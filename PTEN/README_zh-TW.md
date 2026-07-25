# PTEN 基因變異分析 — 全基因組定序（WGS）

分析全基因組定序（WGS）資料，篩檢 **PTEN**（磷酸酶與張力蛋白同源物）基因中的致病性突變。

## 輸入資料

- **檔案**：`your_file.vcf.gz`（173 MB，壓縮 VCF 格式）
- **變異偵測工具**：DeepVariant v1.5.0
- **參考基因組**：GRCh37（hg19）
- **樣本編號**：ULMEDCBB3A73_ULMEDCBB3A73

## 分析方法

1. 從 VCF 中擷取 PTEN 基因區域（`chr10:89,622,870–89,731,687`，GRCh37）所有通過品質篩選（PASS）的變異，共 **35 個變異**。
2. 將變異轉換為 HGVS 命名法，並透過 **Ensembl VEP REST API**（GRCh37 端點）查詢功能影響註解。
3. 針對錯義突變，交叉比對 **ClinVar**（NCBI）與 **gnomAD** 資料庫，確認臨床意義與等位基因頻率。

使用工具：`bcftools`（透過 Homebrew 安裝）、Python 3、Ensembl VEP REST API、NCBI E-utilities。

## 分析結果

**未偵測到致病性或可能致病性的 PTEN 突變。**

### 功能影響摘要

| 影響等級   | 數量 | 說明                                           |
|------------|-----:|------------------------------------------------|
| 高（HIGH）         |    0 | 無截短突變、移碼突變或剪接破壞變異               |
| 中（MODERATE）     |    0 | 無錯義突變                                      |
| 低（LOW）          |    0 | 無同義突變                                      |
| 修飾（MODIFIER）   |   35 | 內含子 / UTR / 上游 / 下游區域（無蛋白質效應）    |

### 結論

在 PTEN 基因中未發現任何編碼區域變異（錯義、無義、移碼或剪接位點變異）。所有偵測到的變異位於內含子、UTR 或側翼區域，預期不會影響 PTEN 蛋白質功能。

## 重現分析

```bash
# 從 VCF 擷取 PTEN 區域變異
gunzip -c your_file.vcf.gz | \
  awk -F'\t' '$1=="chr10" && $2>=89622870 && $2<=89731687 && $7=="PASS"'

# 透過 REST API 查詢 VEP（GRCh37）
# 端點：https://grch37.rest.ensembl.org/vep/human/hgvs/{HGVS_NOTATION}
```

## 免責聲明

本分析為電腦運算結果，非臨床等級之變異解讀。如需做出醫療決策，請諮詢認證遺傳諮詢師或臨床基因檢驗實驗室。
