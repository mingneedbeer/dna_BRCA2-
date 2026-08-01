# WGS Cancer Gene Variant Analysis

Whole-genome sequencing (WGS) data analysis for pathogenic mutations in cancer predisposition genes.

## Project Structure

```
.
├── your_file.vcf.gz          # Raw WGS VCF (DeepVariant v1.5.0, GRCh37)
├── src/
│   └── analyze.py            # VEP annotation pipeline script
├── BRCA2/
├── TP53/
├── RB1/
├── APC/
├── PTEN/
├── KRAS/
├── EGFR/
├── ATM/
├── CHEK2/
├── PALB2/
├── NAFLD/
└── NAFLD_extended/
```

Each gene folder contains `README.md` (English) and `README_zh-TW.md` (Traditional Chinese).

## Gene Analyses

| Gene   | Chromosome | Region (GRCh37)          | PASS Variants | Coding Variants    | Pathogenic |
|--------|-----------|--------------------------|---------------|--------------------|------------|
| BRCA2  | chr13     | 32,889,611–32,973,805   | 68            | 2 (both benign)    | None       |
| TP53   | chr17     | 7,571,720–7,590,868     | 38            | 0                  | None       |
| RB1    | chr13     | 48,877,887–49,056,122   | 226           | 0                  | None       |
| APC    | chr5      | 112,073,554–112,181,936 | 164           | 1 (benign)         | None       |
| PTEN   | chr10     | 89,622,870–89,731,687   | 35            | 0                  | None       |
| KRAS   | chr12     | 25,357,723–25,403,870   | 84            | 0                  | None       |
| EGFR   | chr7      | 55,086,714–55,324,313   | 359           | 1 (benign)         | None       |
| ATM    | chr11     | 108,093,211–108,239,829 | 55            | 1 (benign)         | None       |
| CHEK2  | chr22     | 29,083,731–29,138,410   | 108           | 0                  | None       |
| PALB2  | chr16     | 23,614,488–23,652,631   | 13            | 0                  | None       |

**No pathogenic mutations detected across all 10 genes.**

### NAFLD Risk Variants Check

| Gene | rsID | Location (GRCh37) | Variant | Genotype | Result |
|------|------|-------------------|---------|----------|--------|
| PNPLA3 | rs738409 | chr22:44324727 | I148M (C>G) | **HOM (G/G)** | **Homozygous risk allele ×2** |
| TM6SF2 | rs58542926 | chr19:19379549 | E167K (C>T) | **HOM (T/T)** | **Homozygous risk allele ×2** |
| MBOAT7 | rs641738 | chr19:54676763 | T>C (intronic) | **HET (C/T)** | Heterozygous risk allele ×1 |
| HSD17B13 | rs72613567 | chr4:88231394 | TA-insertion | wild-type | No protective allele |

**High NAFLD genetic risk profile** — homozygous PNPLA3 I148M and TM6SF2 E167K, plus heterozygous MBOAT7. See `NAFLD/` for full details.

### Extended NAFLD Panel (GCKR, MTARC1, APOE, LYPLAL1, GPAM, PNPLA2, CIDEB, TRIB1, MERTK, PEMT)

| Gene | rsID | Variant | Genotype | Result |
|------|------|---------|----------|--------|
| GCKR | rs1260326 | P446L | HET (T/C) | Risk-modifier (population-dependent) |
| MTARC1 | rs2642438 | A165T | HOM (G/G) | Protective ×2 (favourable) |
| APOE | rs429358+rs7412 | ε2/ε3/ε4 | **ε4/ε4** | Homozygous ε4 — clinically relevant |
| LYPLAL1 | rs12137855 | C>T | wild-type | No risk allele |
| GPAM | rs2792751 | I43V | wild-type | No risk allele |
| PNPLA2 | rs1138693 | L481P | HET | Common benign polymorphism |
| CIDEB | (full gene scan) | — | no coding variants | No protective LoF variants |
| TRIB1 | rs2954021/17321515/2954029 | A>G/T | wild-type | No risk allele |
| MERTK | rs34943572 | N329S | HET | Rare, VUS |
| PEMT | rs7946 | V175M | wild-type | No risk allele |

**Notable: APOE ε4/ε4 (homozygous).** See `NAFLD_extended/` for full details.

### Coding Variants Detail

| Gene | Variant (GRCh37) | Genotype | Protein | ClinVar | gnomAD AF | Classification |
|------|-------------------|----------|---------|---------|-----------|----------------|
| BRCA2 | chr13:32906729 A>C (rs144848) | HET | p.Asn372His | Benign (expert panel) | ~24% | Common polymorphism |
| BRCA2 | chr13:32929387 T>C (rs169547) | HOM | p.Val2466Ala | Benign | ~98% | Near-fixed polymorphism |
| APC | chr5:112176756 T>A | HET | p.Val2355Asp | Not in ClinVar | Low | Likely benign |
| EGFR | chr7:55229255 G>A | HET | p.Arg451Lys | Not in ClinVar | Common | Common polymorphism |
| ATM | chr11:108183167 A>G | HOM | p.Asn1497Ser | Not in ClinVar | Common | Common polymorphism |

### Non-coding Variants Summary

| Gene | Total PASS | Intronic | UTR | Upstream/Downstream | Synonymous | Splice-adjacent |
|------|-----------|----------|-----|---------------------|------------|-----------------|
| BRCA2 | 68 | ~50 | ~5 | ~10 | 3 | 0 |
| TP53 | 38 | ~25 | ~1 | ~12 | 0 | 0 |
| RB1 | 226 | ~180 | ~20 | ~25 | 0 | 1 |
| APC | 164 | ~120 | ~5 | ~35 | 4 | 0 |
| PTEN | 35 | ~25 | ~3 | ~7 | 0 | 0 |
| KRAS | 84 | ~60 | ~5 | ~18 | 1 | 0 |
| EGFR | 359 | ~280 | ~15 | ~50 | 4 | 0 |
| ATM | 55 | ~40 | ~5 | ~10 | 0 | 1 |
| CHEK2 | 108 | ~85 | ~5 | ~18 | 0 | 0 |
| PALB2 | 13 | ~10 | ~1 | ~2 | 0 | 0 |

## Method

1. Extract PASS-quality variants from VCF using `awk`
2. Annotate via **Ensembl VEP REST API** (GRCh37 HGVS endpoint)
3. Cross-reference with **ClinVar** and **gnomAD** for clinical significance

### Quick Run

```bash
python src/analyze.py <GENE> <CHROM> <START> <END> your_file.vcf.gz
```

Tools: `bcftools`, Python 3, Ensembl VEP REST API, NCBI E-utilities

## Input

- **File**: `your_file.vcf.gz` (173 MB)
- **Caller**: DeepVariant v1.5.0
- **Reference**: GRCh37 (hg19)
- **Sample**: ULMEDCBB3A73_ULMEDCBB3A73

## Tags

| Tag   | Description                          |
|-------|--------------------------------------|
| v1.0  | Initial BRCA2 analysis               |
| v1.1  | Traditional Chinese README added     |
| v1.2  | Session export log added             |
| v1.3  | Docs reorganized into gene folders   |
| TP53  | TP53 analysis added                  |
| RB1   | RB1 analysis added                   |
| APC   | APC analysis added                   |
| PTEN  | PTEN analysis added                  |
| KRAS  | KRAS analysis added                  |
| EGFR  | EGFR analysis added                  |
| ATM   | ATM analysis added                   |
| CHEK2 | CHEK2 analysis added                 |
| PALB2 | PALB2 analysis added                 |
| v2.0  | Full 10-gene summary tables added    |
| rc-1  | Session export log added             |
| NAFLD | NAFLD core 4-locus panel             |
| NAFLD_extended | Extended NAFLD panel (10 loci) |
| NAFLD_corrected | Core panel corrected (chr-prefix bug fix) |

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
