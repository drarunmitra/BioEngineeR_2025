# ============================================
# Generate Synthetic Datasets
# Data Analysis with R | IISc Bio Engineering
# ============================================

library(tidyverse)
library(here)

# Set seed for reproducibility
set.seed(2025)

# ============================================
# Dataset 1: Clinical Trial Data
# ============================================

clinical_trial <- tibble(
  patient_id = paste0("PT", sprintf("%03d", 1:100)),
  age = round(rnorm(100, 55, 12)),
  sex = sample(c("M", "F"), 100, replace = TRUE, prob = c(0.55, 0.45)),
  bmi = round(rnorm(100, 26, 4), 1),
  treatment = sample(c("Placebo", "Low Dose", "High Dose"), 100,
                     replace = TRUE, prob = c(0.33, 0.33, 0.34)),
  baseline_score = round(rnorm(100, 50, 15)),
  week_4_score = NA_real_,
  week_8_score = NA_real_,
  adverse_event = sample(c(TRUE, FALSE), 100, replace = TRUE, prob = c(0.15, 0.85))
)

# Add treatment effects
clinical_trial <- clinical_trial |>
  mutate(
    treatment_effect = case_when(
      treatment == "Placebo" ~ rnorm(100, 2, 8),
      treatment == "Low Dose" ~ rnorm(100, 10, 10),
      treatment == "High Dose" ~ rnorm(100, 18, 12)
    ),
    week_4_score = round(baseline_score + treatment_effect * 0.5),
    week_8_score = round(baseline_score + treatment_effect),
    change_score = week_8_score - baseline_score,
    responder = change_score > 10
  ) |>
  select(-treatment_effect)

# ============================================
# Dataset 2: Cell Viability Study
# ============================================

cell_study <- tibble(
  sample_id = paste0("S", sprintf("%03d", 1:120)),
  treatment = rep(c("Control", "Drug_A", "Drug_B", "Combo"), each = 30),
  cell_line = rep(rep(c("HeLa", "MCF7", "A549"), each = 10), 4),
  concentration_um = rep(c(0, 10, 25, 50), each = 30),
  viability = c(
    rnorm(30, 95, 5),   # Control
    rnorm(30, 75, 8),   # Drug A
    rnorm(30, 70, 10),  # Drug B
    rnorm(30, 45, 12)   # Combo
  ) |> pmax(0) |> pmin(100),
  apoptosis = NA_real_
) |>
  mutate(
    apoptosis = (100 - viability + rnorm(120, 0, 5)) |> pmax(0) |> pmin(100),
    viability = round(viability, 1),
    apoptosis = round(apoptosis, 1)
  )

# ============================================
# Dataset 3: Gene Expression (simplified)
# ============================================

gene_expression <- tibble(
  sample_id = paste0("GE", sprintf("%03d", 1:60)),
  condition = rep(c("Control", "Treated"), each = 30),
  timepoint = rep(rep(c("0h", "6h", "24h"), each = 10), 2),
  gene_A = c(
    rnorm(30, 100, 15),
    rnorm(30, 180, 25)
  ) |> round(1),
  gene_B = c(
    rnorm(30, 50, 10),
    rnorm(30, 35, 8)
  ) |> round(1),
  gene_C = c(
    rnorm(30, 200, 30),
    rnorm(30, 220, 35)
  ) |> round(1)
)

# ============================================
# Save datasets
# ============================================

write_csv(clinical_trial, here("data", "clinical_trial.csv"))
write_csv(cell_study, here("data", "cell_viability.csv"))
write_csv(gene_expression, here("data", "gene_expression.csv"))

message("Datasets generated and saved to data/ folder")
message("Files created:")
message("  - data/clinical_trial.csv (n=100)")
message("  - data/cell_viability.csv (n=120)")
message("  - data/gene_expression.csv (n=60)")
