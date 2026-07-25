#!/usr/bin/env python3
"""
WGS Cancer Gene Variant Analysis — VEP Annotation Pipeline

Extracts PASS-quality variants from a VCF file for a given gene region,
annotates them using the Ensembl VEP REST API (GRCh37), and reports
functional consequences by impact level.

Usage:
    python src/analyze.py <gene_name> <chrom> <start> <end> <vcf_file>

Example:
    python src/analyze.py BRCA2 13 32889611 32973805 your_file.vcf.gz
"""

import subprocess
import urllib.request
import json
import time
import sys


def make_hgvs(chrom, pos, ref, alt):
    """Convert a variant to HGVS genomic notation."""
    if len(ref) == 1 and len(alt) == 1:
        return f"{chrom}:g.{pos}{ref}>{alt}"
    elif len(ref) > len(alt) and ref.endswith(alt):
        del_start = pos
        del_end = pos + len(ref) - len(alt) - 1
        if del_start == del_end:
            return f"{chrom}:g.{del_start}del"
        return f"{chrom}:g.{del_start}_{del_end}del"
    elif len(alt) > len(ref) and alt.endswith(ref):
        ins_after = pos + len(ref) - 1
        ins_seq = alt[len(ref):]
        return f"{chrom}:g.{ins_after}_{ins_after + 1}ins{ins_seq}"
    else:
        del_start = pos + 1
        del_end = pos + len(ref) - 1
        ins_seq = alt[1:] if len(alt) > 1 else ""
        if del_start <= del_end:
            if ins_seq:
                return f"{chrom}:g.{del_start}_{del_end}delins{ins_seq}"
            return f"{chrom}:g.{del_start}_{del_end}del"
        return f"{chrom}:g.{pos}delins{alt}"


def extract_variants(vcf_file, chrom, start, end):
    """Extract PASS variants from VCF region using awk."""
    chrom_str = f"chr{chrom}" if not str(chrom).startswith("chr") else chrom
    cmd = (
        f"gunzip -c {vcf_file} | "
        f"awk -F'\\t' '$1==\"{chrom_str}\" && $2>={start} && $2<={end} && $7==\"PASS\" "
        f"{{print $2\"\\t\"$4\"\\t\"$5\"\\t\"$10}}'"
    )
    result = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True)
    return result.stdout.strip().split("\n") if result.stdout.strip() else []


def parse_variants(lines, chrom):
    """Parse extracted VCF lines into variant dicts with HGVS notation."""
    variants = []
    for line in lines:
        parts = line.strip().split("\t")
        if len(parts) < 4:
            continue
        pos = int(parts[0])
        ref = parts[1]
        gt = parts[3].split(":")[0]
        for alt in parts[2].split(","):
            variants.append({
                "pos": pos,
                "ref": ref,
                "alt": alt,
                "gt": gt,
                "hgvs": make_hgvs(chrom, pos, ref, alt),
            })
    return variants


def vep_annotate(variants, batch_size=10):
    """Query Ensembl VEP REST API (GRCh37) for HGVS annotations."""
    url = "https://grch37.rest.ensembl.org/vep/human/hgvs"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    all_results = []

    for i in range(0, len(variants), batch_size):
        batch = variants[i:i + batch_size]
        hgvs_list = [v["hgvs"] for v in batch]
        data = json.dumps({"hgvs_notations": hgvs_list}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers)
        try:
            resp = urllib.request.urlopen(req, timeout=60)
            results = json.loads(resp.read().decode())
            all_results.extend(results if isinstance(results, list) else [results])
            print(f"  Batch {i // batch_size + 1}: {len(batch)} variants OK")
        except Exception as e:
            print(f"  Batch {i // batch_size + 1}: ERROR {e}")
            all_results.extend([None] * len(batch))
        time.sleep(0.3)

    return all_results


def extract_gene_consequences(variants, all_results, gene_name):
    """Filter VEP results for a specific gene, deduplicated by HGVS+transcript."""
    gene_variants = []
    seen = set()
    for v, r in zip(variants, all_results):
        if r is None:
            continue
        entries = [r] if isinstance(r, dict) else r if isinstance(r, list) else []
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            tc_list = entry.get("transcript_consequences", [])
            if isinstance(tc_list, dict):
                tc_list = [tc_list]
            for tc in tc_list:
                if not isinstance(tc, dict):
                    continue
                if tc.get("gene_symbol") == gene_name:
                    key = (v["hgvs"], tc.get("transcript_id", ""))
                    if key not in seen:
                        seen.add(key)
                        gene_variants.append({
                            "hgvs": v["hgvs"],
                            "pos": v["pos"],
                            "ref": v["ref"],
                            "alt": v["alt"],
                            "gt": v["gt"],
                            "consequence": tc.get("consequence_terms", ["?"])[0],
                            "impact": tc.get("impact", "?"),
                            "amino_acids": tc.get("amino_acids", ""),
                            "codons": tc.get("codons", ""),
                            "transcript": tc.get("transcript_id", ""),
                        })
    return gene_variants


def summarize(gene_name, gene_variants):
    """Print impact summary and detailed variants by impact level."""
    impact_counts = {}
    for x in gene_variants:
        impact_counts[x["impact"]] = impact_counts.get(x["impact"], 0) + 1

    print(f"\n  Impact summary:")
    for k, v in sorted(impact_counts.items()):
        print(f"    {k}: {v}")

    for level in ["HIGH", "MODERATE", "LOW"]:
        items = [x for x in gene_variants if x["impact"] == level]
        if items:
            print(f"\n  --- {level} IMPACT ---")
            for iv in items:
                zyg = "HET" if "0/" in iv["gt"] else "HOM"
                aa = f" ({iv['amino_acids']})" if iv["amino_acids"] else ""
                codons = f" [{iv['codons']}]" if iv["codons"] else ""
                print(f"    {iv['hgvs']} ({zyg}) | {iv['consequence']}{aa}{codons} | {iv['transcript']}")

    return impact_counts


def main():
    if len(sys.argv) < 6:
        print("Usage: python src/analyze.py <gene_name> <chrom> <start> <end> <vcf_file>")
        sys.exit(1)

    gene_name = sys.argv[1]
    chrom = sys.argv[2]
    start = int(sys.argv[3])
    end = int(sys.argv[4])
    vcf_file = sys.argv[5]

    print(f"=== {gene_name} Analysis ===")
    print(f"  Region: chr{chrom}:{start}-{end}")

    print(f"\n  Extracting PASS variants...")
    lines = extract_variants(vcf_file, chrom, start, end)
    variants = parse_variants(lines, chrom)
    print(f"  Found {len(variants)} variant alleles")

    print(f"\n  Annotating via VEP (GRCh37)...")
    results = vep_annotate(variants)

    gene_vars = extract_gene_consequences(variants, results, gene_name)
    print(f"  {gene_name}-annotated: {len(gene_vars)}")

    impact_counts = summarize(gene_name, gene_vars)

    # Save JSON
    outpath = f"/tmp/{gene_name.lower()}_gene.json"
    with open(outpath, "w") as f:
        json.dump(gene_vars, f, indent=2)
    print(f"\n  Saved to {outpath}")

    # Return summary stats
    return {
        "gene": gene_name,
        "chrom": chrom,
        "start": start,
        "end": end,
        "total_variants": len(variants),
        "impact_counts": impact_counts,
        "gene_annotations": len(gene_vars),
    }


if __name__ == "__main__":
    main()
