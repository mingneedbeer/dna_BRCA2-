# PTEN Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **PTEN** gene (phosphatase and tensin homolog).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the PTEN region (`chr10:89,622,870–89,731,687`, GRCh37) — **35 variants** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3, Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic PTEN mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     0 | No missense variants                      |
| LOW          |     0 | No synonymous variants                    |
| MODIFIER     |    35 | Intronic / UTR / upstream / downstream (no protein effect) |

### Conclusion

No coding-region variants (missense, nonsense, frameshift, or splice-site) were found in the PTEN gene. All detected variants are located in introns, UTRs, or flanking regions and are not expected to affect PTEN protein function.

## Reproducibility

```bash
# Extract PTEN variants from VCF
gunzip -c your_file.vcf.gz | \
  awk -F'\t' '$1=="chr10" && $2>=89622870 && $2<=89731687 && $7=="PASS"'

# Query VEP via REST API (GRCh37)
# Endpoint: https://grch37.rest.ensembl.org/vep/human/hgvs/{HGVS_NOTATION}
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
