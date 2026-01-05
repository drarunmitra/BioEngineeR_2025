#!/usr/bin/env python3
"""
Generate Synthetic Datasets
Data Analysis with R | IISc Bio Engineering
Python version of 01_generate_data.R
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Set seed for reproducibility
np.random.seed(2025)

# ============================================
# Dataset 1: Clinical Trial Data
# ============================================

n_patients = 100

clinical_trial = pd.DataFrame({
    'patient_id': [f"PT{i:03d}" for i in range(1, n_patients + 1)],
    'age': np.round(np.random.normal(55, 12, n_patients)).astype(int),
    'sex': np.random.choice(['M', 'F'], n_patients, p=[0.55, 0.45]),
    'bmi': np.round(np.random.normal(26, 4, n_patients), 1),
    'treatment': np.random.choice(['Placebo', 'Low Dose', 'High Dose'],
                                  n_patients, p=[0.33, 0.33, 0.34]),
    'baseline_score': np.round(np.random.normal(50, 15, n_patients)).astype(int),
    'adverse_event': np.random.choice([True, False], n_patients, p=[0.15, 0.85])
})

# Add treatment effects
def get_treatment_effect(treatment):
    if treatment == 'Placebo':
        return np.random.normal(2, 8)
    elif treatment == 'Low Dose':
        return np.random.normal(10, 10)
    else:  # High Dose
        return np.random.normal(18, 12)

clinical_trial['treatment_effect'] = clinical_trial['treatment'].apply(get_treatment_effect)
clinical_trial['week_4_score'] = np.round(clinical_trial['baseline_score'] +
                                          clinical_trial['treatment_effect'] * 0.5).astype(int)
clinical_trial['week_8_score'] = np.round(clinical_trial['baseline_score'] +
                                          clinical_trial['treatment_effect']).astype(int)
clinical_trial['change_score'] = clinical_trial['week_8_score'] - clinical_trial['baseline_score']
clinical_trial['responder'] = clinical_trial['change_score'] > 10

# Remove temporary column
clinical_trial = clinical_trial.drop('treatment_effect', axis=1)

# ============================================
# Dataset 2: Cell Viability Study
# ============================================

n_samples = 120

cell_study = pd.DataFrame({
    'sample_id': [f"S{i:03d}" for i in range(1, n_samples + 1)],
    'treatment': np.repeat(['Control', 'Drug_A', 'Drug_B', 'Combo'], 30),
    'cell_line': np.tile(np.repeat(['HeLa', 'MCF7', 'A549'], 10), 4),
    'concentration_um': np.repeat([0, 10, 25, 50], 30)
})

# Generate viability data
viability = np.concatenate([
    np.random.normal(95, 5, 30),   # Control
    np.random.normal(75, 8, 30),   # Drug A
    np.random.normal(70, 10, 30),  # Drug B
    np.random.normal(45, 12, 30)   # Combo
])
viability = np.clip(viability, 0, 100)

cell_study['viability'] = np.round(viability, 1)

# Generate apoptosis (inverse relationship with viability + noise)
apoptosis = 100 - viability + np.random.normal(0, 5, n_samples)
apoptosis = np.clip(apoptosis, 0, 100)
cell_study['apoptosis'] = np.round(apoptosis, 1)

# ============================================
# Dataset 3: Gene Expression (simplified)
# ============================================

n_ge_samples = 60

gene_expression = pd.DataFrame({
    'sample_id': [f"GE{i:03d}" for i in range(1, n_ge_samples + 1)],
    'condition': np.repeat(['Control', 'Treated'], 30),
    'timepoint': np.tile(np.repeat(['0h', '6h', '24h'], 10), 2)
})

# Gene A - upregulated in treated
gene_A = np.concatenate([
    np.random.normal(100, 15, 30),  # Control
    np.random.normal(180, 25, 30)   # Treated
])
gene_expression['gene_A'] = np.round(gene_A, 1)

# Gene B - downregulated in treated
gene_B = np.concatenate([
    np.random.normal(50, 10, 30),  # Control
    np.random.normal(35, 8, 30)    # Treated
])
gene_expression['gene_B'] = np.round(gene_B, 1)

# Gene C - slightly upregulated in treated
gene_C = np.concatenate([
    np.random.normal(200, 30, 30),  # Control
    np.random.normal(220, 35, 30)   # Treated
])
gene_expression['gene_C'] = np.round(gene_C, 1)

# ============================================
# Save datasets
# ============================================

data_dir = Path('/home/user/BioEngineeR_2026/data')
data_dir.mkdir(exist_ok=True)

clinical_trial.to_csv(data_dir / 'clinical_trial.csv', index=False)
cell_study.to_csv(data_dir / 'cell_viability.csv', index=False)
gene_expression.to_csv(data_dir / 'gene_expression.csv', index=False)

print("Datasets generated and saved to data/ folder")
print("Files created:")
print(f"  - data/clinical_trial.csv (n={len(clinical_trial)})")
print(f"  - data/cell_viability.csv (n={len(cell_study)})")
print(f"  - data/gene_expression.csv (n={len(gene_expression)})")
