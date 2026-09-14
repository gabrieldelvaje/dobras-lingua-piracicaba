# Tongue Rolling in Piracicaba

A local data story about the observed ability to roll the tongue in a voluntary sample from Piracicaba, Brazil, combining a Google Forms survey, descriptive statistics, a Wilson confidence interval and comparison with published studies.

[Versão em português](README.pt-BR.md)

![Carousel cover](assets/carousel/01-cover.jpeg)

## Research question

**What does a local sample suggest about the frequency of the tongue-rolling phenotype in Piracicaba?**

The survey collected **79 responses**. After normalizing the answer `santa rita` as Piracicaba, following the rule used in the carousel, **73 respondents** were included in the Piracicaba subsample and **6** were treated as residents of other cities.

Among the 73 Piracicaba respondents, **55 answered “Sim”** and **18 answered “Não”**, corresponding to **75.3%** and **24.7%**, respectively. The source export is preserved in this repository and the machine-readable data reproduces the 79 rows from the supplied form export.

## Main findings

- **79** total responses.
- **73** respondents included in the Piracicaba sample.
- **55 of 73 (75.3%)** reported being able to roll the tongue.
- **18 of 73 (24.7%)** reported not being able to roll it.
- The **95% Wilson interval** for the observed proportion is **64.4% to 83.8%**.
- The local result is close to values reported in some published samples, including **72.9%** among Esan participants in southern Nigeria (Ebeye, 2019) and **63.9%** among Nigerian undergraduate students (Adekoya et al., 2020).

## Important interpretation note

This is a **voluntary, non-probability sample**. The 75.3% figure is a descriptive result for the observed Piracicaba subsample. The Wilson interval quantifies binomial uncertainty around that observed proportion, but it does **not** remove selection bias or make the sample statistically representative of the whole municipality.

For that reason, the repository treats the result as a **local sample estimate / data story**, not as an exact population prevalence for Piracicaba.

## Tongue rolling is not a simple Mendelian trait

The traditional classroom explanation of tongue rolling as a single dominant-gene trait is too simplistic. Sturtevant's 1940 paper popularized a hereditary interpretation, but later evidence challenged a simple genetic model. Matlock (1952) reported monozygotic twins discordant for tongue rolling, and Martin (1975) found no evidence supporting a simple genetic basis.

The carousel therefore uses the more cautious expression **observed phenotype** rather than presenting tongue rolling as a one-gene dominant trait.

## Carousel

The seven images below are the original supplied artwork, stored without visual edits.

### 1. Research question
![Slide 1](assets/carousel/01-cover.jpeg)

### 2. How the survey was conducted
![Slide 2](assets/carousel/02-methodology.jpeg)

### 3. Main result
![Slide 3](assets/carousel/03-main-result.jpeg)

### 4. Confidence interval and interpretation
![Slide 4](assets/carousel/04-confidence-interval.jpeg)

### 5. Comparison with published studies
![Slide 5](assets/carousel/05-literature-comparison.jpeg)

### 6. Why this is not a “simple gene”
![Slide 6](assets/carousel/06-not-simple-gene.jpeg)

### 7. Summary
![Slide 7](assets/carousel/07-summary.jpeg)

## Repository structure

```text
assets/carousel/                       original seven carousel images
assets/carousel/SHA256SUMS.txt         hashes of the supplied images
data/respostas_pesquisa.csv            machine-readable survey responses
data/respostas_pesquisa.xlsx           spreadsheet with responses + summary
data/metricas_resumo.csv                key calculated metrics
data/literature_comparison.csv         values shown in the comparison slide
data/source/pesquisa_dobra_lingua_respostas.pdf
                                       original supplied form export
docs/methodology.md
docs/sources.md
docs/data-validation.md
src/validate_metrics.py
```

## Reproducibility

Run the validation script with Python 3:

```bash
python src/validate_metrics.py
```

The script recalculates the sample counts, the 75.3% proportion and the 95% Wilson interval, and checks the normalization rule used for the `santa rita` response.

## Data collection form

Public-facing form URL:

https://docs.google.com/forms/d/1uMHUzyV2TosXmxHaTtNSuZ7NwvCJYoGb74adRUqh9d4/viewform

## Sources

The project documentation includes the supplied survey export and the literature references used in the carousel. See [`docs/sources.md`](docs/sources.md) for full references and links.

## Author

Gabriel Delvaje — data analysis and data storytelling.
