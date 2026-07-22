# Model catalogue data dictionary

`data/models/catalogue.csv` is the public index. It deliberately records only compact original metadata and curator classifications; it is not an equation archive.

| Field | Meaning |
| --- | --- |
| `model_id` | Stable local identifier; never recycled. |
| `model_name` | Source-provided or conventional name, not a claim of authorship. |
| `cell_type` | Controlled vocabulary label in the coverage table. |
| `biological_process` | Process modeled in the cited work. |
| `formalism` | ODE, PDE, hybrid, etc.; source-based classification. |
| `scale` | Molecular, single-cell, population, tissue, or network. |
| `primary_source_doi` | DOI normalized in lower case; empty only for a documented non-DOI source. |
| `persistent_url` | DOI or archival landing page. |
| `bibliography_status` | `verified_bibliography`, `candidate`, or `needs_review`. |
| `equation_status` | `not_extracted`, `extracted`, or `independently_checked`. |
| `implementation_status` | `not_assessed`, `source_linked`, `reproduced`, or `validated`. |
| `license_status` | `not_assessed`, `documented`, or `compatible_for_inclusion`. |
| `curation_note` | Short original note with uncertainty explicitly retained. |

Rows must have a valid DOI URL, unique `model_id`, and values from the declared vocabularies. The validator enforces these constraints.

## 扩展目录

`models/model_catalog.csv` 是与项目完整字段契约兼容的人工维护源文件；`model_catalog.json` 和 `model_catalog.yaml` 由 `python scripts/build_tables.py` 生成。字段中的 `not verified`、`not assessed` 与空的代码位置均是刻意保留的不确定性，不应被视为缺失后可凭猜测补齐。

扩展目录额外记录：

- `model_scope`：`cell_intrinsic`、`cell_function`、`cell_population`、`coupled_multicellular` 或 `indirect_parameterization`；
- `quality_tier`：A–D 的证据层级，而非影响因子或固定引用数；
- `evidence_notes` 与 `limitations`：策展者用原创语言给出的核验边界；
- `code_available`、`code_url`、`code_license`：只有逐一检查外部仓库时才可升级，不能将可访问网页视为可再发布代码。
