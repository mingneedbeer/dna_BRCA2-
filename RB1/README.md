# RB1 Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **RB1** gene (retinoblastoma 1).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the RB1 region (`chr13:48,877,887–49,056,122`, GRCh37) — **226 variants** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3, Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic RB1 mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     0 | No missense variants                      |
| LOW          |     3 | Splice polypyrimidine tract variant (1 position, 3 transcripts) |
| MODIFIER     |   446 | Intronic / UTR / upstream / downstream (no protein effect) |

### Low Impact Variants

| Variant (GRCh37)         | Genotype | Consequence                          | Transcript      |
|--------------------------|----------|--------------------------------------|-----------------|
| chr13:49051481 T>A       | HET (0/1)| splice_polypyrimidine_tract_variant  | ENST00000267163 |
| chr13:49051481 T>A       | HET (0/1)| splice_polypyrimidine_tract_variant  | ENST00000484879 |
| chr13:49051481 T>A       | HET (0/1)| splice_polypyrimidine_tract_variant  | ENST00000531171 |

This variant is in a splice polypyrimidine tract and is classified as LOW impact by VEP — it is not expected to disrupt splicing.

### Conclusion

No coding-region variants (missense, nonsense, frameshift) were found in the RB1 gene. All detected variants are located in introns, UTRs, or flanking regions and are not expected to affect RB1 protein function.

## Reproducibility

```bash
# Extract RB1 variants from VCF
gunzip -c your_file.vcf.gz | \
  awk -F'\t' '$1=="chr13" && $2>=48877887 && $2<=49056122 && $7=="PASS"'

# Query VEP via REST API (GRCh37)
# Endpoint: https://grch37.rest.ensembl.org/vep/human/hgvs/{HGVS_NOTATION}
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
