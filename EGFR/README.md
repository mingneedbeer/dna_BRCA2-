# EGFR Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **EGFR** gene (epidermal growth factor receptor).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the EGFR region (`chr7:55,086,714–55,324,313`, GRCh37) — **359 variant alleles** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3 (`src/analyze.py`), Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic EGFR mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     1 | Missense variant (see below — benign)     |
| LOW          |     4 | Synonymous variants (no protein change)   |
| MODIFIER     |   ~354 | Intronic / UTR / upstream / downstream (no protein effect) |

### Missense Variant

| Variant (GRCh37)         | Genotype | Protein Change   | ClinVar | Notes |
|--------------------------|----------|------------------|---------|-------|
| chr7:55229255 G>A        | HET (0/1)| p.Arg451Lys (R/K) | Not in ClinVar | Common polymorphism |

### Synonymous Variants (4 unique positions)

All synonymous variants are at 4 positions across multiple transcripts — no protein change.

### Conclusion

No pathogenic coding-region variants were found in the EGFR gene. The single missense variant (p.Arg451Lys) is a common polymorphism with no established pathogenicity. All other variants are synonymous or non-coding.

## Reproducibility

```bash
python src/analyze.py EGFR 7 55086714 55324313 your_file.vcf.gz
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
