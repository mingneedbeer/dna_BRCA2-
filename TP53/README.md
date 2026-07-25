# TP53 Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **TP53** gene.

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the TP53 region (`chr17:7,571,720–7,590,868`, GRCh37) — **38 variants** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3, Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic TP53 mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     0 | No missense variants                      |
| LOW          |     0 | No synonymous variants                    |
| MODIFIER     |    38 | Intronic / UTR / upstream / downstream (no protein effect) |

### Variant Categories

All 38 variants fall in non-coding regions of TP53:

| Category                    | Count |
|-----------------------------|------:|
| Intron variants             |   ~25 |
| Upstream gene variants      |   ~8  |
| 3' UTR variants             |   ~1  |
| Non-coding transcript exon  |   ~4  |

### Conclusion

No coding-region variants (missense, nonsense, frameshift, or splice-site) were found in the TP53 gene. All detected variants are located in introns, UTRs, or flanking regions and are not expected to affect TP53 protein function.

## Reproducibility

```bash
# Extract TP53 variants from VCF
gunzip -c your_file.vcf.gz | \
  awk -F'\t' '$1=="chr17" && $2>=7571720 && $2<=7590868 && $7=="PASS"'

# Query VEP via REST API (GRCh37)
# Endpoint: https://grch37.rest.ensembl.org/vep/human/hgvs/{HGVS_NOTATION}
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
