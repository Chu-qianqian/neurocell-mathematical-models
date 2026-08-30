# P1 independent review handoff

The review queue is machine-readable at `data/equations/independent_review_manifest.csv`. It freezes the evidence snapshot at commit `d688703858848257d8c59fd480e0bfb9368d478c` and is portable: every source is identified by a stable public identifier or publication description, not a local path.

## Scope

The queue covers Hodgkin-Huxley, Izhikevich, G-ChI, Morris-Lecar, adaptive exponential integrate-and-fire, and the P1 Amato-Arnold microglial transcription. Each row specifies the audited equation scope, direct-source version, access date, comparison method, difference template, and resolution rule.

## Reviewer procedure

1. Obtain the frozen direct source named in the manifest.
2. Extract the in-scope equations without reading the repository transcription.
3. Compare only after that extraction. Check signs, operators, exponents, subscripts, coefficients, units, locators, initial or boundary conditions, network or event handling, numerical methods, and the related registry rows.
4. For every difference, record: `equation_id`, field, source locator, observed source value, repository value, impact, and proposed correction.
5. Make any resolution in a follow-up commit, record the resolution date, and retain unresolved differences as blockers.

An external reviewer must record their name, role, date, method, source version, access date, target commit, difference result, and resolution in `data/equations/equation_audit.csv`. The mere presence of this package is not an independent review: every record remains below `independently_checked` until that evidence exists.
