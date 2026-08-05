# Hereditary Cancer Predisposition Screen — Clinical Report

## 1. Specimen & Method

| Field | Value |
|-------|-------|
| Sample ID | ULMEDCBB3A73_ULMEDCBB3A73 |
| Test | Hereditary cancer predisposition panel (10 genes) |
| Method | Whole-genome sequencing; computational variant analysis |
| Variant caller | DeepVariant v1.5.0 |
| Reference build | GRCh37 (hg19) |
| Input | `your_file.vcf.gz` (variant-only VCF) |
| Annotation | Ensembl VEP REST API (GRCh37 HGVS), ClinVar, gnomAD |
| Date | See commit history / git tag `v3.0` |

This is a **computational analysis** of research-grade WGS data. It is **not a CLIA-certified clinical test**; all findings should be confirmed by a clinical genetics laboratory before any medical decision.

## 2. Genes Tested

| Gene | Chromosome | Region (GRCh37) |
|------|-----------|------------------|
| BRCA2 | chr13 | 32,889,611–32,973,805 |
| TP53 | chr17 | 7,571,720–7,590,868 |
| RB1 | chr13 | 48,877,887–49,056,122 |
| APC | chr5 | 112,073,554–112,181,936 |
| PTEN | chr10 | 89,622,870–89,731,687 |
| KRAS | chr12 | 25,357,723–25,403,870 |
| EGFR | chr7 | 55,086,714–55,324,313 |
| ATM | chr11 | 108,093,211–108,239,829 |
| CHEK2 | chr22 | 29,083,731–29,138,410 |
| PALB2 | chr16 | 23,614,488–23,652,631 |

## 3. Results

### 3.1 Summary

| Gene | PASS Variants | Coding Variants | Pathogenic |
|------|--------------|-----------------|------------|
| BRCA2 | 68 | 2 (both benign) | **None** |
| TP53 | 38 | 0 | **None** |
| RB1 | 226 | 0 | **None** |
| APC | 164 | 1 (benign) | **None** |
| PTEN | 35 | 0 | **None** |
| KRAS | 84 | 0 | **None** |
| EGFR | 359 | 1 (benign) | **None** |
| ATM | 55 | 1 (benign) | **None** |
| CHEK2 | 108 | 0 | **None** |
| PALB2 | 13 | 0 | **None** |

**No pathogenic (or likely pathogenic) variants detected in any of the 10 cancer predisposition genes.**

### 3.2 Coding Variants Detail

Five coding variants were detected. All are common, benign (or likely benign) polymorphisms; none is disease-causing.

| Gene | Variant (GRCh37) | Genotype | Protein | ClinVar | gnomAD AF | Classification |
|------|-------------------|----------|---------|---------|-----------|----------------|
| BRCA2 | chr13:32906729 A>C (rs144848) | HET | p.Asn372His | Benign (expert panel) | ~24% | Common polymorphism |
| BRCA2 | chr13:32929387 T>C (rs169547) | HOM | p.Val2466Ala | Benign | ~98% | Near-fixed polymorphism |
| APC | chr5:112176756 T>A | HET | p.Val2355Asp | Not in ClinVar | Low | Likely benign |
| EGFR | chr7:55229255 G>A | HET | p.Arg451Lys | Not in ClinVar | Common | Common polymorphism |
| ATM | chr11:108183167 A>G | HOM | p.Asn1497Ser | Not in ClinVar | Common | Common polymorphism |

### 3.3 Non-coding Variants

The remaining PASS variants were intronic, UTR, upstream/downstream, synonymous, or splice-adjacent; none was classified as pathogenic. See the per-gene READMEs and root `README.md` for the full breakdown.

## 4. Interpretation

- No pathogenic or likely pathogenic variants were identified in BRCA2, TP53, RB1, APC, PTEN, KRAS, EGFR, ATM, CHEK2, or PALB2.
- The five coding variants found (Section 3.2) are common population polymorphisms with high allele frequencies and benign/likely benign classifications. They should **not** be reported as clinically significant findings.
- A negative screen does **not** exclude hereditary cancer risk: limitations below, including the absence of phasing, known-copy-number/structural variant limitations, and the possibility of variants outside the interrogated regions.

## 5. Limitations

1. **Not a clinical-grade test** — computational interpretation of research WGS, not CLIA/CAP-validated.
2. **Variant-only VCF** — absence of a variant at a position was assumed to indicate homozygous reference; the sample is a single, unphased individual.
3. **No phasing** — allele phase (cis/trans) is not resolved.
4. **Reference build** — GRCh37 (hg19); coordinates were not lifted to GRCh38.
5. **Coverage & caller limits** — DeepVariant v1.5.0 may miss variants in low-coverage, repetitive, or high-homology regions.
6. **Structural & copy-number variants** — small-variant analysis only; deletions, duplications, and large rearrangements were not comprehensively assessed.
7. **Annotation sources** — ClinVar/gnomAD data are population/evidence-based; classifications may change over time.

## 6. Recommendations

- Confirm findings, if needed, in a **CLIA-certified clinical genetics laboratory** before any medical decision.
- Consult a **certified genetic counselor or clinical genetics professional** for interpretation in the context of personal and family history.
- Discuss an appropriate cancer screening plan with a physician based on family history, regardless of this negative result.

## 7. Considerations for Your Clinician

Framed as observations, not directives:

- The benign coding variants in Section 3.2 are high-frequency SNPs; their incidental presence is expected and not indicative of hereditary cancer risk.
- This analysis did not assess polygenic risk or moderate-penetrance alleles beyond the 10 tested genes.
- Refer to `NAFLD` report (sibling file in this folder) for metabolic findings (APOE ε4/ε4; NAFLD risk profile) that may be relevant to overall clinical care.

## 8. Data Provenance

- Raw data: `your_file.vcf.gz` + `.csi` index (gitignored)
- Pipeline: `src/analyze.py` (VEP GRCh37 annotation)
- Per-gene detailed READMEs: `BRCA2/`, `TP53/`, `RB1/`, `APC/`, `PTEN/`, `KRAS/`, `EGFR/`, `ATM/`, `CHEK2/`, `PALB2/`

## Disclaimer

This document is a computational analysis, not a clinical diagnosis. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
