# Neurocell Mathematical Models — 项目上下文与续接提示词

## 一、项目概述

**仓库**：`https://github.com/Chu-qianqian/neurocell-mathematical-models`
**分支**：`curation/evidence-audit-and-reproducibility`（唯一活跃分支）
**本地路径**：`C:\Users\MSN\Documents\Default Project\repo`
**许可证**：CC-BY-4.0（内容）+ MIT（代码）
**目标**：为神经系统细胞的数学/计算模型建立可溯源的方程转录、变量/参数注册和审计链

## 二、当前进度（截至 v0.2.2）

| 状态 | 数量 | 说明 |
|---|---|---|
| `equation_transcribed` | 9 | 已完成精确源转录并注册变量/参数 |
| `second_pass_checked` | 3 | 已完成转录 + 二次校对 |
| `bibliography_verified` | 13 | 仅有文献引用，方程待转录 |
| **总计** | **25** | |

### 已完成转录的模型（9 条）

| model_id | 提交 | 方程块数 | 变量数 | 参数数 | 来源 |
|---|---|---|---|---|---|
| hopfield_1982 | — | 8 | 18 | 1 | 经典论文 |
| halnes_2013_electrodiffusive_astrocyte | — | 6 | 17 | 14 | PMC 开放全文 |
| polykretis_2018_neural_astrocytic_network | — | 9 | 16 | 15 | Springer 全文 |
| wong_wang_2006_decision | `f9ac30d` | 15 | 22 | 29 | PMC 公式图 |
| morris_lecar_1981 | `af58df7` | 17 | 17 | 17 | 扫描页 CDN 图 |
| brette_gerstner_2005_adex | `a69c5f8` | 4 | 6 | 11 | UCSD 课程镜像 PDF |
| hodgkin_huxley_1952 | — | 23 | 8 | 20 | 经典论文 |
| izhikevich_2003 | — | 2 | 10 | 6 | 经典论文 |
| de_pitta_2009_gchi | — | 17 | 22 | 23 | PMC 全文 |

### 待转录的模型（13 条 bibliography_verified）

| model_id | 模型名 | 细胞类型 | DOI | 全文状态 | 数学形式 |
|---|---|---|---|---|---|
| brunel_2000_ei_network | Brunel 稀疏 E/I 网络 | neural_population | 10.1023/A:1008925309027 | source_identified | hybrid |
| tsodyks_markram_1998_stp | Tsodyks-Markram 短时程突触可塑性 | synapse | 10.1162/089976698300017502 | source_identified | hybrid |
| li_rinzel_1994 | Li-Rinzel 简化 IP3R 钙机制 | astrocyte_relevant_calcium_mechanism | 10.1006/jtbi.1994.1041 | source_identified | ODE |
| potjans_diesmann_2014 | Potjans-Diesmann 皮层微回路 | neural_population | 10.1093/cercor/bhs358 | source_identified | hybrid |
| mrg_2002_myelinated_axon | McIntyre-Richardson-Grill 有髓轴突 | myelinated_axon | 10.1152/jn.00353.2001 | source_identified | ODE |
| jirsa_2014_epileptor | Epileptor 癫痫动力学 | neural_population | 10.1093/brain/awu133 | source_identified | hybrid |
| postnov_2009_neuron_astrocyte | Postnov 神经元-星形胶质体模型 | mixed_neuron_astrocyte_system | 10.1007/s10867-009-9156-x | source_identified | ODE |
| amato_arnold_2025_microglia | Amato 小胶质细胞缺血半暗带模型 | microglia | 10.1016/j.mbs.2025.109549 | not_verified | ODE |
| nikolov_2022_oligodendrocyte | Nikolov 少突胶质细胞分化动力学 | oligodendrocyte | 10.3390/math10162928 | not_verified | ODE |
| neuron_astrocyte_associative_memory_2025 | 神经元-星形胶质体联想记忆 | mixed_neuron_astrocyte_system | 10.1073/pnas.2417788122 | source_identified | ODE |
| astrocyte_place_cell_formation_2022 | 星形胶质体位置细胞形成 | mixed_neuron_astrocyte_system | 10.1007/s10827-022-00828-6 | source_identified | hybrid |
| polykretis_astrocytic_microdomain | Polykretis 星形胶质体微域模型 | mixed_neuron_astrocyte_system | 10.1007/978-3-030-05587-5_15 | source_identified | hybrid |
| sequence_learning_neuronal_astrocytic_network | 神经元-星形胶质体序列学习 | mixed_neuron_astrocyte_system | 10.1007/978-3-030-59277-6_32 | source_identified | ODE |

## 三、核心架构规则

### 3.1 文件结构

```
models/model_catalog.csv          ← 唯一手工维护的规范文件
equations/models/<model_id>.md    ← 方程转录页（一个模型一个文件）
data/equations/equation_audit.csv ← 方程审计行
data/equations/variable_registry.csv
data/equations/parameter_registry.csv
references/verification_audit.csv ← 模型级验证审计
scripts/build_tables.py           ← 生成 references.csv, README 等
implementations/brian2/           ← Brian2 参考实现
```

### 3.2 枚举词汇表

`models/schema.json` 定义了所有 CSV 字段的允许值。**绝不能**编造不在枚举中的值。

### 3.3 验证管道（按顺序运行）

```powershell
$py = "C:\Users\MSN\AppData\Local\Temp\opencode\py312\python.exe"
& $py scripts\validate_catalogue.py
& $py scripts\build_tables.py
& $py scripts\validate_references.py
& $py scripts\validate_equations.py
& $py scripts\validate_links.py
& $py scripts\validate_language.py
& $py -m unittest discover -s tests
```

**全部绿灯才能提交。**

### 3.4 $$ 块规则

`equations/models/<id>.md` 中的 `$$` 块数量 **必须 ≤** `equation_audit.csv` 中该模型的审计行数，且逐一对应。多出的 `$$` 块会触发 validate_equations.py 失败。

### 3.5 语言规则

- 所有仓库文本 **必须英文**（仅 `scripts/i18n_zh.py` 和 `*.zh-CN.md` 例外）
- validate_language.py 会检查所有文件

### 3.6 Git 身份

```bash
git -c user.name="Chu-qianqian" -c user.email="287763656+Chu-qianqian@users.noreply.github.com" commit -m "..."
```

提交前缀：`data:`, `docs:`, `model:`, `release:`, `test:`

### 3.7 网络与代理

- GitHub / arXiv：本地可访问
- NCBI 主站 / NCBI PMC：被墙
- `cdn.ncbi.nlm.nih.gov`：可访问（用于拉公式图和扫描页）
- Clash TUN 模式：`127.0.0.1:53000`
- `raw.githubusercontent.com`：不稳定

## 四、方程转录工作流（每条模型）

### 步骤 1：获取全文

优先级：
1. PMC 开放全文（XML 或扫描页）
2. 课程/作者托管 PDF
3. arXiv 预印本
4. Springer/Nature/Elsevier 等出版商全文

获取方式：
- `webfetch` 抓取 HTML，找公式图片 URL（`cdn.ncbi.nlm.nih.gov/...gif`）
- 扫描页：用 pymupdf (`fitz`) 渲染 PDF 为 PNG，视觉读取
- Python：`C:\Users\MSN\AppData\Local\Temp\opencode\py312\python.exe`

### 步骤 2：识别方程

- 为每个编号方程建立独立 `$$` 块
- 未编号但独立的显示公式也建立 `$$` 块
- 每个 `$$` 块在 audit 中有一行

### 步骤 3：写方程转录页

结构（参考 wong_wang_2006_decision.md、morris_lecar_1981.md）：

```markdown
# Model Name

## Verification status
## Scope
## Source citation
## Variables
（表格：Symbol | Meaning | Units | Source status）
## Parameters
（表格：Parameter | Meaning | Units | Value/range | Provenance）
## Equations
（$$ 块，精确转录，保留原文编号）
## Term-by-term interpretation
（逐项解读）
## Inputs, outputs, and conditions
## Assumptions and limitations
## Experimental support
## Reproducibility and code
```

### 步骤 4：更新 CSV

用 Python 脚本追加：
- `equation_audit.csv`：每个 $$ 块一行
- `variable_registry.csv`：每个变量一行
- `parameter_registry.csv`：每个参数一行
- `model_catalog.csv`：更新 equation_status 等字段
- `verification_audit.csv`：equations_inspected=yes

### 步骤 5：验证 + 提交

```powershell
& $py scripts\validate_catalogue.py
& $py scripts\build_tables.py
& $py scripts\validate_references.py
& $py scripts\validate_equations.py
& $py scripts\validate_links.py
& $py scripts\validate_language.py
& $py -m unittest discover -s tests
# 全绿后
git add -A && git commit -m "data: transcribe <Model Name> equations"
git push origin curation/evidence-audit-and-reproducibility
```

## 五、发版流程（每批 3-4 条转录后）

1. CHANGELOG.md 加新版本段落
2. CITATION.cff 更新 `version` 和 `date-released`
3. 验证 + 提交 + 推送
4. `git tag -a vX.Y.Z -m "..." && git push origin vX.Y.Z`
5. 用户在网页创建 GitHub Release（选 tag）
6. Zenodo 自动出草稿 → 用户 Publish
7. 用户把新 DOI 发给助手 → 写入 CITATION.cff 和 README 徽章

版本号规则：
- 0.2.0 → 中文 i18n
- 0.2.1 → 首批 3 条转录
- 0.2.2 → 本次 3 条转录
- 下一批 3-4 条 → 0.2.3 或 0.3.0

## 六、关键经验与反模式

### ✅ 做

- 精确转录，即使发现原文有排印错误也要转录并在 interpretation 中标注
- 从官方代码仓库获取参数（如 wong_wang_2006 的 xjwanglab）
- 每次写完一个模型就跑完整验证
- 保留原文编号，不要重新编号

### ❌ 不做

- 绝不编造方程或参数值
- 绝不在 audit 行数少于 $$ 块数时提交
- 绝不留下 AI 工具痕迹（中文注释、临时文件、过时文件）
- 绝不在验证管道有错误时提交
- 绝不修改 `scripts/` 或 `tests/` 目录下的文件（除非用户明确要求）

## 七、推荐继续顺序

按依赖复杂度和可用全文排序：

| 优先级 | model_id | 理由 |
|---|---|---|
| 1 | brunel_2000_ei_network | 经典网络模型，方程简洁，可能有 arXiv |
| 2 | tsodyks_markram_1998_stp | 经典 STP 模型，方程明确 |
| 3 | li_rinzel_1994 | 经典钙动力学，PMC 可能有全文 |
| 4 | potjans_diesmann_2014 | 大规模网络，方程复杂但规范 |
| 5 | mrg_2002_myelinated_axon | 经典有髓轴突模型 |
| 6 | jirsa_2014_epileptor | 癫痫动力学，方程已知 |
| 7-13 | 其余 7 条 | 按可用全文情况灵活处理 |

## 八、续接对话提示词

将以下内容粘贴到新对话的首条消息中：

---

**我正在为 neurocell-mathematical-models 仓库进行方程转录工作（P1 pipeline）。项目状态：25 个模型中已完成 9 个方程转录（v0.2.2），还有 13 个 bibliography_verified 模型待转录。**

**请先读取以下文件了解项目结构：**
1. `C:\Users\MSN\Documents\Default Project\repo\models\model_catalog.csv` — 规范模型目录
2. `C:\Users\MSN\Documents\Default Project\repo\models\schema.json` — 枚举词汇表
3. `C:\Users\MSN\Documents\Default Project\repo\equations\models\wong_wang_2006_decision.md` — 转录页模板（参考）
4. `C:\Users\MSN\Documents\Default Project\repo\equations\models\morris_lecar_1981.md` — 转录页模板（参考）
5. `C:\Users\MSN\Documents\Default Project\repo\data\equations\equation_audit.csv` — 审计行格式
6. `C:\Users\MSN\Documents\Default Project\repo\data\equations\variable_registry.csv` — 变量注册格式
7. `C:\Users\MSN\Documents\Default Project\repo\data\equations\parameter_registry.csv` — 参数注册格式

**待转录的 13 个模型（按推荐顺序）：**
1. brunel_2000_ei_network — DOI: 10.1023/A:1008925309027
2. tsodyks_markram_1998_stp — DOI: 10.1162/089976698300017502
3. li_rinzel_1994 — DOI: 10.1006/jtbi.1994.1041
4. potjans_diesmann_2014 — DOI: 10.1093/cercor/bhs358
5. mrg_2002_myelinated_axon — DOI: 10.1152/jn.00353.2001
6. jirsa_2014_epileptor — DOI: 10.1093/brain/awu133
7. postnov_2009_neuron_astrocyte — DOI: 10.1007/s10867-009-9156-x
8. amato_arnold_2025_microglia — DOI: 10.1016/j.mbs.2025.109549
9. nikolov_2022_oligodendrocyte — DOI: 10.3390/math10162928
10. neuron_astrocyte_associative_memory_2025 — DOI: 10.1073/pnas.2417788122
11. astrocyte_place_cell_formation_2022 — DOI: 10.1007/s10827-022-00828-6
12. polykretis_astrocytic_microdomain — DOI: 10.1007/978-3-030-05587-5_15
13. sequence_learning_neuronal_astrocytic_network — DOI: 10.1007/978-3-030-59277-6_32

**工作流程：**
1. 对每个模型：获取全文 → 识别方程 → 写转录页 → 更新 CSV → 验证 → 提交
2. 验证命令（PowerShell）：
```powershell
$py = "C:\Users\MSN\AppData\Local\Temp\opencode\py312\python.exe"
& $py scripts\validate_catalogue.py && & $py scripts\build_tables.py && & $py scripts\validate_references.py && & $py scripts\validate_equations.py && & $py scripts\validate_links.py && & $py scripts\validate_language.py && & $py -m unittest discover -s tests 2>&1 | Select-Object -Last 3
```
3. Git 身份：`git -c user.name="Chu-qianqian" -c user.email="287763656+Chu-qianqian@users.noreply.github.com" commit -m "data: transcribe <Model Name> equations"`

**关键规则：**
- $$ 块数 ≤ audit 行数，1:1 对应
- 所有内容必须英文
- 精确转录原文公式，排印错误在 interpretation 中标注
- 验证全绿才能提交
- NCBI 被墙，用 cdn.ncbi.nlm.nih.gov 拉公式图
- Python 解释器：`C:\Users\MSN\AppData\Local\Temp\opencode\py312\python.exe`
- 每 3-4 条转录后统一发版（CHANGELOG + CITATION.cff + tag + Release）

**已完成转录的提交历史：**
- `f9ac30d` — wong_wang_2006（15 块）
- `af58df7` — morris_lecar_1981（17 块）
- `a69c5f8` — brette_gerstner_2005_adex（4 块）

---

## 九、常用脚本模板

### 追加审计行 + 变量 + 参数

```python
import csv, os

ROOT = r"C:\Users\MSN\Documents\Default Project\repo"
DATE = "YYYY-MM-DD"
MODEL = "model_id"
PAGE = "equations/models/model_id.md"
VSOURCE = "来源描述"
SID = "来源标识"
VERSION = "年份"

audit_rows = [
    ("eq_id_1", "描述", "文献定位"),
]

variables = [
    ("symbol", "meaning", "units", "locator"),
]

parameters = [
    ("param", "meaning", "units", "value", "provenance", "registered"),
]

# 追加 audit
with open(os.path.join(ROOT, "data", "equations", "equation_audit.csv"), encoding="utf-8", newline="") as h:
    existing = {r["equation_id"] for r in csv.DictReader(h)}
with open(os.path.join(ROOT, "data", "equations", "equation_audit.csv"), "a", encoding="utf-8", newline="") as h:
    w = csv.writer(h, lineterminator="\r\n")
    for eq_id, label, loc in audit_rows:
        if eq_id in existing: raise SystemExit(f"dup: {eq_id}")
        w.writerow([eq_id, MODEL, PAGE, label, loc, VSOURCE, "exact_verified_transcription", "equation_transcribed", DATE, "", "", "", SID, VERSION, DATE, "not_verified", "", "", "", ""])

# 追加变量
with open(os.path.join(ROOT, "data", "equations", "variable_registry.csv"), encoding="utf-8", newline="") as h:
    ev = {(r["model_id"], r["symbol"]) for r in csv.DictReader(h)}
with open(os.path.join(ROOT, "data", "equations", "variable_registry.csv"), "a", encoding="utf-8", newline="") as h:
    w = csv.writer(h, lineterminator="\r\n")
    for sym, meaning, units, loc in variables:
        if (MODEL, sym) in ev: raise SystemExit(f"dup: {sym}")
        w.writerow([MODEL, sym, meaning, units, "source_verified", loc, DATE])

# 追加参数
with open(os.path.join(ROOT, "data", "equations", "parameter_registry.csv"), encoding="utf-8", newline="") as h:
    ep = {(r["model_id"], r["parameter"]) for r in csv.DictReader(h)}
with open(os.path.join(ROOT, "data", "equations", "parameter_registry.csv"), "a", encoding="utf-8", newline="") as h:
    w = csv.writer(h, lineterminator="\r\n")
    for param, meaning, units, val, prov, status in parameters:
        if (MODEL, param) in ep: raise SystemExit(f"dup: {param}")
        w.writerow([MODEL, param, meaning, units, val, prov, status, DATE])
```

### 更新 model_catalog.csv

```python
import csv, os

ROOT = r"C:\Users\MSN\Documents\Default Project\repo"
MODEL = "model_id"

updates = {
    "equation_status": "equation_transcribed",
    "equation_source_locator": "定位描述",
    "equation_verification_source": "来源描述",
    "equation_transcription_type": "exact_verified_transcription",
    "variable_registry_status": "registered",
    "parameter_registry_status": "registered",
    "full_text_access_status": "source_inspected",
    "event_handling_status": "source_located",
    "event_handling_locator": "reset 规则定位",
    "evidence_notes": "转录说明",
    "last_verified": "YYYY-MM-DD",
}

CATALOG = os.path.join(ROOT, "models", "model_catalog.csv")
with open(CATALOG, encoding="utf-8", newline="") as h:
    reader = csv.DictReader(h)
    rows = list(reader)
target = [r for r in rows if r["model_id"] == MODEL]
if len(target) != 1: raise SystemExit(f"expected 1, got {len(target)}")
target[0].update(updates)
with open(CATALOG, "w", encoding="utf-8", newline="") as h:
    w = csv.DictWriter(h, fieldnames=reader.fieldnames, lineterminator="\r\n")
    w.writeheader()
    w.writerows(rows)
```

## 十、Zenodo DOI 更新

发版后用户会提供新 DOI，需要用以下脚本更新 CITATION.cff 和 README：

```python
# 读取 CITATION.cff，替换 identifiers 部分
# 读取 README.md 和 README.zh-CN.md，更新 DOI 徽章
# 提交：git commit -m "docs: record Zenodo DOI vX.Y.Z"
```
