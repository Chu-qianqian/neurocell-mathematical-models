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
