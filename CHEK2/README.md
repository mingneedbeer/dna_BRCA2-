# CHEK2 Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **CHEK2** gene (checkpoint kinase 2).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the CHEK2 region (`chr22:29,083,731–29,138,410`, GRCh37) — **108 variant alleles** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3 (`src/analyze.py`), Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic CHEK2 mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     0 | No missense variants                      |
| LOW          |     0 | No synonymous variants                    |
| MODIFIER     |  2397 | Intronic / UTR / upstream / downstream (no protein effect) |

### Conclusion

No coding-region variants (missense, nonsense, frameshift, or splice-site) were found in the CHEK2 gene. All detected variants are in introns, UTRs, or flanking regions and are not expected to affect CHEK2 protein function.

## Reproducibility

```bash
python src/analyze.py CHEK2 22 29083731 29138410 your_file.vcf.gz
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
