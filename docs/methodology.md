# Methodology / Metodologia

## 1. Data collection

The primary dataset comes from a short Google Forms survey asking two questions:

1. whether the respondent can roll the tongue as shown in the survey image;
2. whether the respondent lives in Piracicaba.

The supplied export contains 79 responses collected between 11 August 2026 and 25 August 2026. The repository preserves the supplied PDF export in `data/source/` and reproduces its rows in CSV/XLSX form.

## 2. Geographic inclusion rule

The answer `santa rita` in the residence field was treated as Piracicaba because the carousel explicitly states: “Santa Rita foi considerada Piracicaba”. All literal `Sim` responses were also included as Piracicaba; literal `Não` responses were treated as other cities.

This yields:

- 79 total responses;
- 73 included in the Piracicaba subsample;
- 6 outside the Piracicaba subsample.

## 3. Main proportion

Within the Piracicaba subsample:

- 55 respondents answered `Sim` to the tongue-rolling question;
- 18 answered `Não`;
- observed proportion = 55 / 73 = 0.7534246575 = 75.3%.

## 4. Confidence interval

The carousel reports a 95% confidence interval of 64.4% to 83.8%. This repository reproduces that interval using the Wilson score interval for a binomial proportion with:

- x = 55 successes;
- n = 73 observations;
- z = 1.95996398454.

The Wilson interval is preferred here over the simple Wald interval because it behaves better for finite binomial samples.

## 5. Interpretation limits

The sample was voluntary and no probability sampling design is documented. Therefore:

- 75.3% is a descriptive estimate for the observed sample;
- the Wilson interval describes binomial sampling uncertainty conditional on the observed sample model;
- the interval does not account for self-selection, coverage bias, demographic imbalance or other selection effects;
- the project should not present 75.3% as the exact prevalence in Piracicaba.

## 6. Literature comparison

The comparison slide is descriptive rather than a meta-analysis. It places the Piracicaba sample beside reported proportions from published studies with different populations, sampling designs and contexts. The values should therefore be read as contextual references, not as directly exchangeable estimates of the same target population.
