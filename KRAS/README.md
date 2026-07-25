# KRAS Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **KRAS** gene (KRAS proto-oncogene, GTPase).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the KRAS region (`chr12:25,357,723–25,403,870`, GRCh37) — **84 variant alleles** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3 (`src/analyze.py`), Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic KRAS mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     0 | No missense variants                      |
| LOW          |     1 | Synonymous variant (no protein change)    |
| MODIFIER     |  ~83 | Intronic / UTR / upstream / downstream (no protein effect) |

### Synonymous Variant

| Variant (GRCh37)          | Genotype | Protein Change | Notes |
|---------------------------|----------|----------------|-------|
| chr12:25368462 C>T        | HOM (1/1)| p.Arg (synonymous) | No amino acid change |

### Conclusion

No pathogenic coding-region variants were found in the KRAS gene. The single synonymous variant does not change the protein sequence. All other variants are non-coding.

## Reproducibility

```bash
python src/analyze.py KRAS 12 25357723 25403870 your_file.vcf.gz
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
