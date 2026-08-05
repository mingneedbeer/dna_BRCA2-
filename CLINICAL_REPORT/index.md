# Clinical Report — Index

Consolidated clinical-style summary of the whole-genome sequencing (WGS) analysis for sample **ULMEDCBB3A73_ULMEDCBB3A73** (DeepVariant v1.5.0, GRCh37).

## Reports

| Report | Coverage | Headline Finding |
|--------|----------|------------------|
| [cancer.md](./cancer.md) | 10 cancer predisposition genes (BRCA2, TP53, RB1, APC, PTEN, KRAS, EGFR, ATM, CHEK2, PALB2) | **No pathogenic variants detected** |
| [nafld.md](./nafld.md) | NAFLD core 4-locus + extended 10-locus panel (incl. APOE) | **High NAFLD genetic risk profile**; **APOE ε4/ε4** |

## Headline Findings

1. **Hereditary cancer screen: negative.** No pathogenic or likely pathogenic variants across all 10 genes. The 5 coding variants found are common benign polymorphisms (e.g., BRCA2 N372H ~24%, V2466A ~98%, ATM N1497S).
2. **NAFLD: high genetic risk.** PNPLA3 I148M **G/G** (homozygous), TM6SF2 E167K **T/T** (homozygous), MBOAT7 rs641738 **HET**, HSD17B13 protective allele absent. Partially offset by MTARC1 A165T **G/G** (protective ×2).
3. **APOE ε4/ε4 (homozygous).** Clinically relevant for Alzheimer's, cardiovascular, and hepatic fat risk.

## Reading Notes

- Each report follows a clinical structure: **Specimen & Method → Results → Interpretation → Limitations → Recommendations → Considerations for Your Clinician → Data Provenance**.
- **Recommendations** are generic referrals (counseling, CLIA confirmation).
- **Considerations for Your Clinician** are specific observations, framed as data, not medical directives.
- This is a **computational analysis, not a CLIA-certified clinical test**.

## Related Resources

- Root project README: [`../README.md`](../README.md) (EN) and [`../README_zh-TW.md`](../README_zh-TW.md)
- Per-gene detail: `../BRCA2/`, `../TP53/`, `../RB1/`, `../APC/`, `../PTEN/`, `../KRAS/`, `../EGFR/`, `../ATM/`, `../CHEK2/`, `../PALB2/`
- NAFLD detail: `../NAFLD/`, `../NAFLD_extended/`
- Pipeline: `../src/analyze.py`

## Disclaimer

This document is a computational analysis, not a clinical diagnosis. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
