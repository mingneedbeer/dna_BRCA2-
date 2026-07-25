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
└── PALB2/
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

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
