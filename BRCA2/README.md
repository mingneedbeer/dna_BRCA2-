# BRCA2 Mutation Analysis — WGS VCF

Analysis of whole-genome sequencing (WGS) data to screen for pathogenic mutations in the **BRCA2** gene.

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Extracted all PASS-quality variants in the BRCA2 region (`chr13:32,889,611–32,973,805`, GRCh37) — **68 variants** found.
2. Converted variants to HGVS notation and queried the **Ensembl VEP REST API** (GRCh37 endpoint) for functional consequence annotations.
3. Cross-referenced missense variants against **ClinVar** (NCBI) and **gnomAD** for clinical significance and allele frequency.

Tools used: `bcftools` (installed via Homebrew), Python 3, Ensembl VEP REST API, NCBI E-utilities.

## Results

**No pathogenic or likely pathogenic BRCA2 mutations were detected.**

### Impact Summary

| Impact       | Count | Description                               |
|--------------|------:|-------------------------------------------|
| HIGH         |     0 | No truncating, frameshift, or splice-disrupting variants |
| MODERATE     |     2 | Missense variants (both benign — see below) |
| LOW          |     3 | Synonymous (no protein change)             |
| MODIFIER     |   ~63 | Intronic / UTR (no protein effect)         |

### Missense Variants

Both missense variants are **benign polymorphisms** commonly found in the general population.

| Variant (GRCh37)         | dbSNP     | Genotype | Protein Change     | ClinVar         | gnomAD AF | Notes                                |
|--------------------------|-----------|----------|--------------------|-----------------|-----------|--------------------------------------|
| chr13:32906729 A>C       | rs144848  | HET (0/1)| p.Asn372His (N372H)| **Benign** (expert panel) | ~24%  | Common polymorphism; functional assays confirm not pathogenic |
| chr13:32929387 T>C       | rs169547  | HOM (1/1)| p.Val2466Ala (V2466A)| **Benign**     | ~98%      | Near-fixed polymorphism; OncoKB: "likely neutral" |

### Variant Details

- **N372H (rs144848)**: Found in ~24% of populations globally. ClinVar classifies as Benign with expert panel review (ENIGMA). Functional assays classify as IARC Class 1 (not pathogenic). Located in exon 10, outside the DNA-binding domain.

- **V2466A (rs169547)**: One of the most common BRCA2 variants at ~98% allele frequency. ClinVar classifies as Benign. Located in the FANCD2 interaction domain. OncoKB assessment: "likely neutral."

## Reproducibility

```bash
# Extract BRCA2 variants from VCF
gunzip -c your_file.vcf.gz | \
  awk -F'\t' '$1=="chr13" && $2>=32889611 && $2<=32973805 && $7=="PASS"'

# Query VEP via REST API (GRCh37)
# Endpoint: https://grch37.rest.ensembl.org/vep/human/hgvs/{HGVS_NOTATION}
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
