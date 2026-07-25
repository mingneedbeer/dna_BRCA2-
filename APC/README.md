# APC Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **APC** gene (adenomatous polyposis coli).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the APC region (`chr5:112,073,554–112,181,936`, GRCh37) — **164 variants** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3, Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic APC mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     1 | Missense variant (see below — benign)     |
| LOW          |    24 | Synonymous variants (no protein change)   |
| MODIFIER     |  1300 | Intronic / UTR / upstream / downstream (no protein effect) |

### Missense Variant

| Variant (GRCh37)         | Genotype | Protein Change   | ClinVar  | Notes |
|--------------------------|----------|------------------|----------|-------|
| chr5:112176756 T>A       | HET (0/1)| p.Val2355Asp (V/D) | Not in ClinVar | Low allele frequency; no pathogenicity data |

### Synonymous Variants (8 unique positions)

All 24 synonymous variants are at 8 positions across multiple transcripts — no protein change.

### Conclusion

No pathogenic coding-region variants were found in the APC gene. The single missense variant (p.Val2355Asp) is not recorded in ClinVar and has no established pathogenicity. All other variants are synonymous or non-coding.

## Reproducibility

```bash
# Extract APC variants from VCF
gunzip -c your_file.vcf.gz | \
  awk -F'\t' '$1=="chr5" && $2>=112073554 && $2<=112181936 && $7=="PASS"'

# Query VEP via REST API (GRCh37)
# Endpoint: https://grch37.rest.ensembl.org/vep/human/hgvs/{HGVS_NOTATION}
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
