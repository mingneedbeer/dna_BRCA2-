# NAFLD Risk Variants Check — WGS VCF

Analysis of whole-genome sequencing (WGS) data for four well-established non-alcoholic fatty liver disease (NAFLD) susceptibility variants.

## Input

- **File**: `your_file.vcf.gz` (173 MB, compressed VCF)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Method

1. Resolved GRCh37 coordinates for each rsID via **Ensembl VEP REST API** (GRCh37 endpoint).
2. Searched the VCF for variants at each position (VCF is variant-only, so absence = homozygous reference).
3. Interpreted genotype at each locus.

## Variants Checked

| Gene | rsID | Location (GRCh37) | Variant | Consequence |
|------|------|-------------------|---------|-------------|
| PNPLA3 | rs738409 | chr22:44324727 | C>G (I148M) | NAFLD risk (G allele) |
| TM6SF2 | rs58542926 | chr19:19379549 | C>T (E167K) | NAFLD risk (T allele) |
| MBOAT7 | rs641738 | chr19:54676763 | C>T (3'UTR) | NAFLD risk (T allele) |
| HSD17B13 | rs72613567 | chr4:88231394 | TA-insertion | NAFLD protective |

## Results

| Gene | rsID | Genotype | Interpretation |
|------|------|----------|----------------|
| PNPLA3 | rs738409 | **HOM (G/G)** | **Homozygous I148M risk allele (×2)** |
| TM6SF2 | rs58542926 | **HOM (T/T)** | **Homozygous E167K risk allele (×2)** |
| MBOAT7 | rs641738 | **HET (C/T)** | Heterozygous risk allele (×1) |
| HSD17B13 | rs72613567 | wild-type | No protective TA-insertion allele |

### Conclusion

**The sample carries a high genetic risk profile for NAFLD:**

- **PNPLA3 I148M G/G** — the single strongest genetic risk factor for NAFLD; homozygous carriage markedly increases steatosis, NASH, fibrosis, and HCC risk (risk conferred independent of obesity).
- **TM6SF2 E167K T/T** — homozygous loss-of-function; increases hepatic lipid retention and NAFLD risk, though it lowers serum lipids (cardioprotective).
- **MBOAT7 rs641738 T** — heterozygous risk allele; associated with reduced MBOAT7 expression and increased NAFLD/NASH progression risk.
- **HSD17B13 TA-insertion** — absent; the sample does not carry this protective allele.

Carrying risk alleles at three loci (PNPLA3, TM6SF2, MBOAT7) places the sample in a high polygenic risk category for NAFLD progression.

## Reproducibility

```bash
# Check each locus (example):
gunzip -c your_file.vcf.gz | awk -F'\t' '$1=="chr22" && $2>=44324720 && $2<=44324735 && !/^#/'
gunzip -c your_file.vcf.gz | awk -F'\t' '$1=="chr19" && $2>=19379542 && $2<=19379557 && !/^#/'
```

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. NAFLD risk is polygenic and gene-environment interactive; these results indicate genetic susceptibility, not a diagnosis. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
