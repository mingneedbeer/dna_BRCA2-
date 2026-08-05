# Metabolic / NAFLD Risk Panel — Clinical Report

## 1. Specimen & Method

| Field | Value |
|-------|-------|
| Sample ID | ULMEDCBB3A73_ULMEDCBB3A73 |
| Test | NAFLD genetic susceptibility panel (core 4-locus + extended 10-locus) |
| Method | Whole-genome sequencing; computational variant analysis |
| Variant caller | DeepVariant v1.5.0 |
| Reference build | GRCh37 (hg19) |
| Input | `your_file.vcf.gz` (variant-only VCF) |
| Annotation | Ensembl VEP REST API (GRCh37), gnomAD |
| Date | See commit history / git tag `v3.0` |

This is a **computational analysis** of research-grade WGS data. It is **not a CLIA-certified clinical test**; all findings should be confirmed by a clinical genetics laboratory before any medical decision.

## 2. Panel Tested

**Core panel:** PNPLA3, TM6SF2, MBOAT7, HSD17B13
**Extended panel:** GCKR, MTARC1, APOE, LYPLAL1, GPAM, TRIB1, PEMT, plus gene-region scans of PNPLA2, CIDEB, MERTK

## 3. Results

### 3.1 Core 4-Locus Panel

| Gene | rsID | Location (GRCh37) | Variant | Genotype | Result |
|------|------|-------------------|---------|----------|--------|
| PNPLA3 | rs738409 | chr22:44324727 | I148M (C>G) | **HOM (G/G)** | **Homozygous risk allele ×2** |
| TM6SF2 | rs58542926 | chr19:19379549 | E167K (C>T) | **HOM (T/T)** | **Homozygous risk allele ×2** |
| MBOAT7 | rs641738 | chr19:54676763 | T>C (3'UTR) | **HET (C/T)** | Heterozygous risk allele ×1 |
| HSD17B13 | rs72613567 | chr4:88231394 | TA-insertion | wild-type | No protective allele |

### 3.2 Extended Panel

| Gene | rsID | Variant | Genotype | Result |
|------|------|---------|----------|--------|
| GCKR | rs1260326 | P446L | HET (T/C) | Risk-modifier (population-dependent) |
| MTARC1 | rs2642438 | A165T | HOM (G/G) | Protective ×2 (favourable) |
| APOE | rs429358 + rs7412 | ε2/ε3/ε4 | **ε4/ε4** | Homozygous ε4 — clinically relevant |
| LYPLAL1 | rs12137855 | C>T | wild-type | No risk allele |
| GPAM | rs2792751 | I43V | wild-type | No risk allele |
| TRIB1 | rs2954021/17321515/2954029 | A>G/T | wild-type | No risk allele |
| PEMT | rs7946 | V175M | wild-type | No risk allele |

### 3.3 Gene-Region Coding-Variant Scans

| Gene | PASS alleles | Missense | Interpretation |
|------|--------------|----------|----------------|
| PNPLA2 | 10 | p.Leu481Pro (rs1138693, HET) | Common polymorphism (AF ~0.70), benign |
| CIDEB | 8 | 0 | No protective LoF variants |
| MERTK | 88 | p.Asn329Ser (rs34943572, HET) | Rare (AF ~0.0004), VUS; not the established NASH-fibrosis protective variant |

### 3.4 APOE ε4/ε4 (Dedicated Section)

- rs429358: **C/C**
- rs7412: **C/C**
- **Haplotype: ε4/ε4 (homozygous)**

The ε4 allele is the most significant finding of this panel:
- **Alzheimer's disease**: ~12× increased risk for homozygotes vs ε3/ε3.
- **Cardiovascular disease**: elevated LDL cholesterol and coronary heart disease risk.
- **Hepatic**: increased hepatic fat content and NAFLD risk.
- It is a common polymorphism with population-level risk associations, **not a diagnosis**.

## 4. Interpretation

- The sample carries a **high genetic risk profile for NAFLD**: homozygous PNPLA3 I148M (G/G) — the single strongest NAFLD genetic risk factor — plus homozygous TM6SF2 E167K (T/T), heterozygous MBOAT7 rs641738, and **no** HSD17B13 protective allele. Risk alleles at three core loci place the sample in a high polygenic risk category for NAFLD progression (steatosis, NASH, fibrosis, HCC).
- Partially offsetting: **MTARC1 A165T G/G** (protective ×2) and GCKR P446L HET (direction population-dependent). TM6SF2 E167K lowers serum lipids (cardioprotective).
- **APOE ε4/ε4** is independently clinically relevant (Alzheimer's, cardiovascular, hepatic fat).
- MERTK p.Asn329Ser (HET) is a rare VUS; PNPLA2 p.Leu481Pro is a benign common polymorphism. Neither is a recognized NAFLD risk/protective variant.

## 5. Limitations

1. **Not a clinical-grade test** — computational interpretation of research WGS, not CLIA/CAP-validated.
2. **Variant-only VCF** — absence of a variant at a position was assumed to indicate homozygous reference.
3. **No phasing** — APOE haplotype was inferred from genotype, not resolved by phasing.
4. **Reference build** — GRCh37 (hg19); coordinates not lifted to GRCh38.
5. **Polygenic, gene-environment interaction** — these results indicate genetic susceptibility, not a diagnosis of NAFLD or disease.
6. **Population-based associations** — effect sizes and directions are population-dependent and may change with updated evidence.

## 6. Recommendations

- Confirm findings in a **CLIA-certified clinical genetics laboratory** before any medical decision.
- Discuss this report with a **physician** in the context of liver enzymes, lipids, and overall metabolic health.
- **Not a diagnosis**: genetic susceptibility alone does not establish NAFLD or any disease.

## 7. Considerations for Your Clinician

Framed as observations that may merit investigation, not directives:

- Given the homozygous PNPLA3 + TM6SF2 + MBOAT7 risk profile: consider **liver enzyme assessment and hepatic-fibrosis/steatosis screening** (e.g., imaging-based measures).
- Given APOE ε4/ε4: consider **lipid panel and cardiovascular risk assessment**, and discuss the Alzheimer's-disease risk implication in the appropriate setting.
- **Lifestyle observations** that plausibly mitigate NAFLD progression given the genetic profile: alcohol avoidance/minimization, weight management, and regular physical activity.
- MERTK p.Asn329Ser is a VUS; no immediate action is indicated, but it should be revisited as evidence accumulates.

## 8. Data Provenance

- Core panel: `NAFLD/`
- Extended panel: `NAFLD_extended/`
- Pipeline: `src/analyze.py` (VEP GRCh37 annotation)
- Raw data: `your_file.vcf.gz` + `.csi` index (gitignored)

## Disclaimer

This document is a computational analysis, not a clinical diagnosis. NAFLD risk is polygenic and gene-environment interactive; APOE ε4/ε4 is a common polymorphism with population-level risk associations. For medical decisions, consult a certified genetic counselor, physician, or clinical genetics laboratory.
