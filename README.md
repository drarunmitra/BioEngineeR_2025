# Data Analysis with R

**3-Day Workshop | IISc Bio Engineering | January 6-8, 2025**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

A hands-on R workshop for biomedical data analysis covering:

| Day | Theme | Topics |
|-----|-------|--------|
| 1 | R Foundations | RStudio, tidyverse, dplyr, ggplot2 |
| 2 | Statistics | t-tests, ANOVA, correlation, regression |
| 3 | Reporting | Publication figures, Quarto, mini-project |

## Quick Start

```r
install.packages(c("tidyverse", "here", "gtsummary", "patchwork", "broom"))
```

## Build

```bash
Rscript R/00_generate_datasets.R
quarto render
```

## Author

Dr. Arun Mitra, IISc Bio Engineering

## License

CC-BY-4.0
