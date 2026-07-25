# PALB2 Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **PALB2** gene (partner and localizer of BRCA2).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the PALB2 region (`chr16:23,614,488–23,652,631`, GRCh37) — **13 variant alleles** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3 (`src/analyze.py`), Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic PALB2 mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     0 | No missense variants                      |
| LOW          |     0 | No synonymous variants                    |
| MODIFIER     |    45 | Intronic / UTR / upstream / downstream (no protein effect) |

### Conclusion

No coding-region variants (missense, nonsense, frameshift, or splice-site) were found in the PALB2 gene. All detected variants are in introns, UTRs, or flanking regions and are not expected to affect PALB2 protein function.

## Reproducibility

```bash
python src/analyze.py PALB2 16 23614488 23652631 your_file.vcf.gz
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
