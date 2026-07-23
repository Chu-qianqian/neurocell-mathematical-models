# Evidence-status migration

## Purpose

The initial catalogue used `independently_checked` for three equation records without storing a named independent checker, check date, method, source version, or discrepancy resolution. The strict audit contract introduced on 2026-07-23 does not permit that evidence gap.

## Conservative migration

The following records were changed from `independently_checked` to `second_pass_checked`:

- Hodgkin-Huxley 1952;
- Izhikevich 2003;
- De Pittà G-ChI 2009.

Their lawful source locators, displayed equations, variable rows, parameter rows, and equation-audit rows were retained. The status change does not assert that the transcriptions are wrong; it states that the repository cannot demonstrate an independent review.

No record currently has `independently_checked` status. A future promotion requires all independent-check fields in `data/equations/equation_audit.csv`, including a named checker, date, method, verification source, source version, source access date, discrepancy result, and discrepancy resolution.

## Holding-record promotion

Wilson-Cowan 1972 and Montbrio-Pazo-Roxin 2015 were promoted from bibliography-only holding records to `equation_transcribed` after inspection of lawful primary-source full text and recording of exact equation locators. They remain below `second_pass_checked`, have incomplete parameter registries, and have no executed implementation or reproduction claim.
