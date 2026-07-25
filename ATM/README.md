# ATM Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **ATM** gene (ataxia telangiectasia mutated).

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the ATM region (`chr11:108,093,211–108,239,829`, GRCh37) — **55 variant alleles** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3 (`src/analyze.py`), Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic ATM mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     1 | Missense variant (see below — benign)     |
| LOW          |     1 | Splice polypyrimidine tract variant       |
| MODIFIER     |   ~53 | Intronic / UTR / upstream / downstream (no protein effect) |

### Missense Variant

| Variant (GRCh37)          | Genotype | Protein Change   | ClinVar | Notes |
|---------------------------|----------|------------------|---------|-------|
| chr11:108183167 A>G       | HOM (1/1)| p.Asn1497Ser (N/S) | Not in ClinVar | Common polymorphism |

### Low Impact Variant

| Variant (GRCh37)          | Genotype | Consequence                          |
|---------------------------|----------|--------------------------------------|
| chr11:108202154 delinsCT  | HET (0/1)| splice_polypyrimidine_tract_variant  |

### Conclusion

No pathogenic coding-region variants were found in the ATM gene. The missense variant (p.Asn1497Ser) is a common polymorphism. The splice polypyrimidine tract variant is classified as LOW impact by VEP and is not expected to disrupt splicing.

## Reproducibility

```bash
python src/analyze.py ATM 11 108093211 108239829 your_file.vcf.gz
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
