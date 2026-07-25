# WGS Cancer Gene Variant Analysis

Whole-genome sequencing (WGS) data analysis for pathogenic mutations in cancer predisposition genes.

## Project Structure

```
.
├── your_file.vcf.gz          # Raw WGS VCF (DeepVariant v1.5.0, GRCh37)
├── BRCA2/                    # BRCA2 gene analysis
│   ├── README.md
│   ├── README_zh-TW.md
│   └── session-ses_067c.md
└── TP53/                     # TP53 gene analysis
    ├── README.md
    ├── README_zh-TW.md
    └── session-ses_067c.md
```

## Gene Analyses

| Gene  | Chromosome | Region (GRCh37)        | PASS Variants | Coding Variants | Pathogenic |
|-------|-----------|------------------------|---------------|-----------------|------------|
| BRCA2 | chr13     | 32,889,611–32,973,805 | 68            | 2 (both benign) | None       |
| TP53  | chr17     | 7,571,720–7,590,868   | 38            | 0               | None       |

## Method

1. Extract PASS-quality variants from VCF using `awk`
2. Annotate via **Ensembl VEP REST API** (GRCh37 HGVS endpoint)
3. Cross-reference with **ClinVar** and **gnomAD** for clinical significance

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

## Disclaimer

This is a computational analysis, not a clinical-grade variant interpretation. For medical decisions, consult a certified genetic counselor or clinical genetics laboratory.
