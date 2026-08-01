# NAFLD Risk Variants Check — WGS VCF

Analysis of whole-genome sequencing (WGS) data for four well-established non-alcoholic fatty liver disease (NAFLD) susceptibility variants.

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Resolved GRCh37 coordinates for each rsID via **Ensembl VEP REST API** (GRCh37 endpoint).
2. Searched the VCF for variants at each position (500 bp windows; VCF is variant-only, so absence = homozygous reference).
3. Interpreted genotype at each locus.

## Variants Checked

| Gene | rsID | Location (GRCh37) | Variant | Consequence |
|------|------|-------------------|---------|-------------|
| PNPLA3 | rs738409 | chr22:44324727 | C>G (I148M) | NAFLD risk (G allele) |
| TM6SF2 | rs58542926 | chr19:19379549 | C>T (E167K) | NAFLD risk (T allele) |
| MBOAT7 | rs641738 | chr19:54676763 | T>C (intronic) | NAFLD risk (C allele) |
| HSD17B13 | rs72613567 | chr4:88231394 | TA-insertion | NAFLD protective |

## Results

**None of the four variants were detected in the VCF.**

| Gene | rsID | Genotype | Interpretation |
|------|------|----------|----------------|
| PNPLA3 | rs738409 | wild-type | No I148M risk allele |
| TM6SF2 | rs58542926 | wild-type | No E167K risk allele |
| MBOAT7 | rs641738 | wild-type | No rs641738 risk allele |
| HSD17B13 | rs72613567 | wild-type | No protective TA-insertion allele |

### Conclusion

The sample carries **no** NAFLD risk alleles at these four established loci, nor the protective HSD17B13 TA-insertion allele. All four loci are homozygous reference (wild-type).

## Reproducibility

```bash
# Check each locus (example):
gunzip -c your_file.vcf.gz | awk -F'\t' '$1=="22" && $2>=44324500 && $2<=44325000 && !/^#/'
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. NAFLD risk is polygenic; these loci are modifiers, not determinants. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
