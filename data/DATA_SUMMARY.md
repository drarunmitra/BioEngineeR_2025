# Synthetic Biomedical Datasets - Summary Report

**Generated:** 2026-01-05
**Project:** BioEngineeR 2026 - Data Analysis with R Workshop
**Institution:** IISc Bio Engineering

---

## Overview

This document summarizes three synthetic biomedical datasets created for teaching purposes. All datasets include realistic value ranges, appropriate correlations, and are fully reproducible (seed: 2025).

## Dataset 1: Clinical Trial Data

**File:** `data/clinical_trial.csv`
**Size:** 100 patients
**Purpose:** Teaching clinical trial analysis, treatment comparisons, and outcome assessment

### Variables

| Variable | Type | Description | Range/Values |
|----------|------|-------------|--------------|
| patient_id | Character | Unique patient identifier | PT001-PT100 |
| age | Numeric | Patient age in years | 28-81 years |
| sex | Categorical | Patient sex | M (47%), F (53%) |
| bmi | Numeric | Body Mass Index | 16.5-34.6 |
| treatment | Categorical | Treatment group assignment | Placebo (38%), Low Dose (35%), High Dose (27%) |
| baseline_score | Numeric | Disease severity score at baseline | 0-100 scale |
| week_4_score | Numeric | Disease severity score at week 4 | 0-100 scale |
| week_8_score | Numeric | Disease severity score at week 8 | 0-100 scale |
| change_score | Numeric | Change from baseline to week 8 | Calculated |
| responder | Logical | Responder status (change > 10) | TRUE/FALSE |
| adverse_event | Logical | Any adverse event reported | TRUE (16%), FALSE (84%) |

### Key Findings

- **Mean age:** 53.2 years (SD: 11.2)
- **Treatment effects** (mean change from baseline):
  - Placebo: 1.3 points
  - Low Dose: 11.1 points
  - High Dose: 18.8 points
- **Overall responder rate:** 44.0%
- **Adverse event rate:** 16.0%
- **Missing data:** None

### Visualizations

See `figures/clinical_trial_analysis.png` for:
- Age and BMI distributions
- Treatment group sizes
- Treatment effect comparisons (boxplots)
- Responder rates by treatment
- Baseline vs Week 8 score correlation

### Teaching Applications

- ANOVA and pairwise comparisons
- Linear regression with covariates
- Logistic regression for binary outcomes
- Visualization of treatment effects
- Intent-to-treat analysis concepts

---

## Dataset 2: Cell Viability Study

**File:** `data/cell_viability.csv`
**Size:** 120 samples
**Purpose:** Teaching in vitro drug screening analysis and dose-response relationships

### Variables

| Variable | Type | Description | Range/Values |
|----------|------|-------------|--------------|
| sample_id | Character | Unique sample identifier | S001-S120 |
| treatment | Categorical | Drug treatment | Control, Drug_A, Drug_B, Combo |
| cell_line | Categorical | Cell line used | HeLa, MCF7, A549 |
| concentration_um | Numeric | Drug concentration in µM | 0, 10, 25, 50 |
| viability | Numeric | Cell viability percentage | 0-100% |
| apoptosis | Numeric | Apoptosis percentage | 0-100% |

### Experimental Design

- **Balanced design:** 4 treatments × 3 cell lines × 10 replicates = 120 samples
- **Treatment groups:** 30 samples each
- **Cell lines:** 40 samples each (HeLa, MCF7, A549)
- **Concentrations:** Equal representation

### Key Findings

**Mean viability by treatment:**
- Control: 95.7% (minimal toxicity)
- Drug A: 72.0% (moderate effect)
- Drug B: 68.6% (moderate effect)
- Combination: 44.0% (strong synergistic effect)

**Mean apoptosis by treatment:**
- Control: 5.2%
- Drug A: 29.2%
- Drug B: 32.3%
- Combination: 54.9%

**Viability by cell line:**
- HeLa: 71.0%
- MCF7: 71.0%
- A549: 68.2%

- **Missing data:** None
- **Inverse relationship:** Viability and apoptosis are inversely correlated (expected biological pattern)

### Visualizations

See `figures/cell_viability_analysis.png` for:
- Viability boxplots by treatment
- Apoptosis boxplots by treatment
- Cell line comparisons
- Viability vs apoptosis scatter plot

### Teaching Applications

- Two-way ANOVA (treatment × cell line)
- Drug synergy analysis
- Dose-response curves
- Data transformation (proportions, logit)
- Multiple testing corrections

---

## Dataset 3: Gene Expression Study

**File:** `data/gene_expression.csv`
**Size:** 60 samples
**Purpose:** Teaching differential gene expression analysis and longitudinal comparisons

### Variables

| Variable | Type | Description | Range/Values |
|----------|------|-------------|--------------|
| sample_id | Character | Unique sample identifier | GE001-GE060 |
| condition | Categorical | Treatment condition | Control, Treated |
| timepoint | Categorical | Time of sample collection | 0h, 6h, 24h |
| gene_A | Numeric | Gene A expression level | Arbitrary units |
| gene_B | Numeric | Gene B expression level | Arbitrary units |
| gene_C | Numeric | Gene C expression level | Arbitrary units |

### Experimental Design

- **Balanced design:** 2 conditions × 3 timepoints × 10 replicates = 60 samples
- **Control samples:** 30
- **Treated samples:** 30
- **Each timepoint:** 20 samples

### Key Findings

**Mean expression by condition:**

*Control:*
- Gene A: 104.9 ± 14.0
- Gene B: 50.3 ± 9.7
- Gene C: 195.8 ± 28.5

*Treated:*
- Gene A: 182.4 ± 19.6 (↑)
- Gene B: 33.8 ± 8.3 (↓)
- Gene C: 212.7 ± 35.4 (↑)

**Fold changes (Treated vs Control):**
- **Gene A:** 1.74× (**upregulated** - likely induced by treatment)
- **Gene B:** 0.67× (**downregulated** - likely suppressed by treatment)
- **Gene C:** 1.09× (slightly upregulated - minimal response)

- **Missing data:** None

### Visualizations

See `figures/gene_expression_analysis.png` for:
- Individual gene expression boxplots (Control vs Treated)
- Fold change annotations
- Expression trajectories over time
- Multi-gene comparisons

### Teaching Applications

- t-tests and Wilcoxon tests
- Volcano plots and fold change analysis
- Time series analysis
- Principal component analysis (PCA)
- Heatmap visualizations
- Introduction to RNA-seq concepts

---

## Data Quality

### Reproducibility
- **Random seed:** 2025 (set in generation scripts)
- **Generation script:** `scripts/01_generate_data.R` (R version)
- **Python equivalent:** `scripts/generate_data.py`

### Missing Data
All three datasets have **no missing values** by design for introductory teaching purposes. Advanced exercises could introduce missing data mechanisms (MCAR, MAR, MNAR).

### Realistic Features
- Appropriate distributional assumptions (normal, binomial)
- Biologically plausible correlations
- Realistic effect sizes for teaching
- Balanced experimental designs
- Representative sample sizes

---

## Files Generated

### Data Files
```
data/
├── clinical_trial.csv      (100 rows, 11 columns)
├── cell_viability.csv      (120 rows, 6 columns)
└── gene_expression.csv     (60 rows, 6 columns)
```

### Visualization Files
```
figures/
├── clinical_trial_analysis.png
├── cell_viability_analysis.png
└── gene_expression_analysis.png
```

### Scripts
```
scripts/
├── 01_generate_data.R          # R data generation
├── generate_data.py            # Python data generation
├── explore_datasets.py         # Data exploration
└── visualize_datasets.py       # Visualization generation
```

---

## Usage in R

### Loading Data

```r
library(tidyverse)
library(here)

# Load datasets
clinical <- read_csv(here("data", "clinical_trial.csv"))
cell <- read_csv(here("data", "cell_viability.csv"))
gene <- read_csv(here("data", "gene_expression.csv"))

# Quick inspection
glimpse(clinical)
summary(cell)
head(gene)
```

### Basic Analysis Examples

```r
# Clinical trial: Compare treatments
clinical |>
  group_by(treatment) |>
  summarize(
    n = n(),
    mean_change = mean(change_score),
    responder_rate = mean(responder)
  )

# Cell viability: Treatment effect
cell |>
  group_by(treatment) |>
  summarize(
    mean_viability = mean(viability),
    sd_viability = sd(viability)
  )

# Gene expression: Differential expression
gene |>
  group_by(condition) |>
  summarize(across(starts_with("gene"), mean))
```

---

## Citation

When using these datasets in educational materials:

```
Synthetic biomedical datasets generated for BioEngineeR 2026 Workshop
Indian Institute of Science (IISc), Department of Bio Engineering
For educational purposes only. Not based on real patient data.
```

---

## Notes for Instructors

### Strengths
- Clean, complete data ideal for learning
- Realistic effect sizes and distributions
- Multiple analysis opportunities per dataset
- Suitable for progressive complexity teaching

### Limitations (Intentional)
- No missing data (simplified for beginners)
- Perfectly balanced designs (real data rarely is)
- Clear treatment effects (real effects often subtle)
- Single outcome measures (real studies more complex)

### Extension Opportunities
- Introduce missing data mechanisms
- Add confounders and covariates
- Simulate measurement error
- Create unbalanced/messy versions
- Add time-to-event outcomes
- Incorporate multi-level structures

---

**End of Report**
