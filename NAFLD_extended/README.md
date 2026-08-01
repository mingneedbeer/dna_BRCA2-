# NAFLD Extended Panel — WGS VCF

Extended non-alcoholic fatty liver disease (NAFLD) susceptibility variant analysis beyond the core 4-locus panel (see `NAFLD/`).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Resolved GRCh37 coordinates for each rsID via **Ensembl VEP REST API** (GRCh37 endpoint).
2. Scanned the VCF for variants at each locus and across full gene regions (PNPLA2, CIDEB, MERTK) using `awk` single-pass extraction.
3. Annotated gene-region variants via **Ensembl VEP** and cross-referenced **gnomAD** for allele frequency.

## Results

### Established NAFLD Risk/Protective Variants

| Gene | rsID | Location (GRCh37) | Variant | Genotype | Interpretation |
|------|------|-------------------|---------|----------|----------------|
| GCKR | rs1260326 | chr2:27730940 | P446L (T>C) | **HET (T/C)** | Risk-modifier; effect direction population-dependent |
| MTARC1 | rs2642438 | chr1:220970028 | A165T (A>G) | **HOM (G/G)** | Protective allele ×2 (favourable) |
| APOE | rs429358 | chr19:45411941 | Arg112Cys (T>C) | **HOM (C/C)** | See ε2/ε3/ε4 below |
| APOE | rs7412 | chr19:45412079 | Arg176Cys (C>T) | **HOM (C/C)** | See ε2/ε3/ε4 below |
| LYPLAL1 | rs12137855 | chr1:219448378 | C>T | wild-type | No risk allele |
| GPAM | rs2792751 | chr10:113940329 | I43V (T>C) | wild-type | No risk allele |
| TRIB1 | rs2954021 | chr8:126482077 | A>G | wild-type | No risk allele |
| TRIB1 | rs17321515 | chr8:126486409 | A>G/T | wild-type | No risk allele |
| TRIB1 | rs2954029 | chr8:126490972 | A>T | wild-type | No risk allele |
| PEMT | rs7946 | chr17:17409560 | V175M (C>T) | wild-type | No risk allele |

### APOE ε2/ε3/ε4 Haplotype

APOE haplotypes are defined by the two SNPs: **ε2** (rs429358-T, rs7412-T), **ε3** (rs429358-T, rs7412-C), **ε4** (rs429358-C, rs7412-C).

- rs429358: **C/C**
- rs7412: **C/C**

**Result: APOE ε4/ε4 (homozygous).**

The ε4 allele is associated with increased risk of Alzheimer's disease (~12× for homozygotes vs ε3/ε3), cardiovascular disease, and — relevant to liver — increased hepatic fat content and NAFLD risk. This is the most significant finding in this panel and warrants clinical discussion.

### Gene-Region Coding-Variant Scans

| Gene | Region (GRCh37) | PASS alleles | Missense | Interpretation |
|------|-----------------|--------------|----------|----------------|
| PNPLA2 | chr11:818,902–825,573 | 10 | 1 (p.Leu481Pro, rs1138693, HET) | Common polymorphism (gnomAD AF ~0.70), benign |
| CIDEB | chr14:24,774,302–24,780,636 | 8 | 0 | No rare CIDEB variants (no protective LoF) |
| MERTK | chr2:112,656,056–112,787,138 | 88 | 1 (p.Asn329Ser, rs34943572, HET) | Rare (gnomAD AF ~0.0004), not the established NASH-fibrosis protective variant |

PNPLA2 p.Leu481Pro (rs1138693) and MERTK p.Asn329Ser (rs34943572) are both heterozygous missense variants; neither is a recognized NAFLD risk/protective variant. MERTK N329S is rare but present in gnomAD (AF ~0.0003–0.0004), including homozygotes, suggesting no strong pathogenicity.

## Summary

| Category | Finding |
|----------|---------|
| Risk alleles (GCKR, LYPLAL1, GPAM, TRIB1, PEMT) | GCKR P446L HET only; all others wild-type |
| Protective alleles | **MTARC1 A165T G/G (2 copies)** |
| APOE | **ε4/ε4 — homozygous, clinically relevant** |
| Rare coding variants | MERTK N329S HET (VUS), PNPLA2 L481P HET (benign common) |
| CIDEB | No variants |

## Reproducibility

```bash
python3 src/analyze.py PNPLA2 chr11 818902 825573 your_file.vcf.gz
python3 src/analyze.py CIDEB chr14 24774302 24780636 your_file.vcf.gz
python3 src/analyze.py MERTK chr2 112656056 112787138 your_file.vcf.gz
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. The APOE ε4/ε4 finding is a common polymorphism with population-level risk associations, not a diagnosis. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
