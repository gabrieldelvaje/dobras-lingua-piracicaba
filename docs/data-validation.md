# Data validation notes

## Supplied response export

The supplied PDF contains 79 rows. The reconstructed CSV/XLSX preserves:

- timestamp;
- answer to the tongue-rolling question;
- original answer to the Piracicaba residence question;
- normalized Piracicaba indicator used by the carousel analysis.

The original answer `santa rita` is intentionally preserved in the raw-response column and normalized to `Sim` only in the separate normalized field.

## Recalculated counts

The repository validation reproduces the values shown in the carousel:

| Metric | Value |
|---|---:|
| Total responses | 79 |
| Piracicaba sample | 73 |
| Other cities | 6 |
| Piracicaba: can roll tongue | 55 |
| Piracicaba: cannot roll tongue | 18 |
| Observed proportion | 75.3% |
| Wilson 95% lower bound | 64.4% |
| Wilson 95% upper bound | 83.8% |

## Important statistical caveat

The numerical Wilson interval is correctly reproduced for 55/73, but the sample is voluntary rather than a documented random/probability sample. Consequently, the interval must not be interpreted as guaranteeing 95% population coverage for all residents of Piracicaba. It does not quantify selection bias.

## Literature slide

The literature comparison uses values exactly as displayed in the supplied carousel where possible:

- Piracicaba: 75.3%;
- Ebeye / Esan sample: 72.9%;
- Sturtevant (1940): approximately 70%;
- Lagos / Adekoya et al. (2020): 63.9%.

The studies differ in population, sample size and design. No pooled estimate is calculated.

## Genetic interpretation

The repository does not label tongue rolling as a validated single-gene dominant trait. Later twin and genetic evidence cited in the project is inconsistent with that simple classroom model. The preferred wording is **observed phenotype**.
