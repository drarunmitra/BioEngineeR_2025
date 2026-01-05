#!/usr/bin/env python3
"""
Explore Generated Datasets
Data Analysis with R | IISc Bio Engineering
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ============================================
# Dataset 1: Clinical Trial Data
# ============================================

print("=" * 70)
print("CLINICAL TRIAL DATASET")
print("=" * 70)

clinical = pd.read_csv('/home/user/BioEngineeR_2026/data/clinical_trial.csv')

print("\n📊 DATASET SHAPE:")
print(f"   Rows: {clinical.shape[0]}, Columns: {clinical.shape[1]}")

print("\n📋 COLUMN INFORMATION:")
print(clinical.dtypes)

print("\n👀 FIRST 10 ROWS:")
print(clinical.head(10))

print("\n📈 SUMMARY STATISTICS (Numeric Variables):")
print(clinical.describe())

print("\n🔍 CATEGORICAL VARIABLES:")
for col in ['sex', 'treatment', 'adverse_event', 'responder']:
    if col in clinical.columns:
        print(f"\n{col}:")
        print(clinical[col].value_counts())
        print(f"  Proportions:")
        print(clinical[col].value_counts(normalize=True).round(3))

print("\n🚫 MISSING DATA:")
missing = clinical.isnull().sum()
if missing.sum() == 0:
    print("   No missing data!")
else:
    print(missing[missing > 0])

print("\n💡 KEY INSIGHTS:")
print(f"   • Average age: {clinical['age'].mean():.1f} years (SD: {clinical['age'].std():.1f})")
print(f"   • Average baseline score: {clinical['baseline_score'].mean():.1f}")
print(f"   • Treatment groups:")
for treatment in clinical['treatment'].unique():
    n = (clinical['treatment'] == treatment).sum()
    mean_change = clinical[clinical['treatment'] == treatment]['change_score'].mean()
    print(f"     - {treatment}: n={n}, mean change = {mean_change:.1f}")
print(f"   • Overall responder rate: {(clinical['responder'].sum() / len(clinical) * 100):.1f}%")
print(f"   • Adverse event rate: {(clinical['adverse_event'].sum() / len(clinical) * 100):.1f}%")

# ============================================
# Dataset 2: Cell Viability Study
# ============================================

print("\n\n" + "=" * 70)
print("CELL VIABILITY DATASET")
print("=" * 70)

cell = pd.read_csv('/home/user/BioEngineeR_2026/data/cell_viability.csv')

print("\n📊 DATASET SHAPE:")
print(f"   Rows: {cell.shape[0]}, Columns: {cell.shape[1]}")

print("\n📋 COLUMN INFORMATION:")
print(cell.dtypes)

print("\n👀 FIRST 10 ROWS:")
print(cell.head(10))

print("\n📈 SUMMARY STATISTICS:")
print(cell.describe())

print("\n🔍 EXPERIMENTAL DESIGN:")
print(f"\nTreatment groups:")
print(cell['treatment'].value_counts().sort_index())
print(f"\nCell lines:")
print(cell['cell_line'].value_counts().sort_index())
print(f"\nConcentrations (µM):")
print(cell['concentration_um'].value_counts().sort_index())

print("\n🚫 MISSING DATA:")
missing = cell.isnull().sum()
if missing.sum() == 0:
    print("   No missing data!")
else:
    print(missing[missing > 0])

print("\n💡 KEY INSIGHTS:")
print("\nMean viability by treatment:")
for treatment in cell['treatment'].unique():
    mean_viab = cell[cell['treatment'] == treatment]['viability'].mean()
    mean_apop = cell[cell['treatment'] == treatment]['apoptosis'].mean()
    print(f"   • {treatment}: viability = {mean_viab:.1f}%, apoptosis = {mean_apop:.1f}%")

print("\nViability by cell line:")
for line in cell['cell_line'].unique():
    mean_viab = cell[cell['cell_line'] == line]['viability'].mean()
    print(f"   • {line}: {mean_viab:.1f}%")

# ============================================
# Dataset 3: Gene Expression
# ============================================

print("\n\n" + "=" * 70)
print("GENE EXPRESSION DATASET")
print("=" * 70)

gene = pd.read_csv('/home/user/BioEngineeR_2026/data/gene_expression.csv')

print("\n📊 DATASET SHAPE:")
print(f"   Rows: {gene.shape[0]}, Columns: {gene.shape[1]}")

print("\n📋 COLUMN INFORMATION:")
print(gene.dtypes)

print("\n👀 FIRST 10 ROWS:")
print(gene.head(10))

print("\n📈 SUMMARY STATISTICS:")
print(gene.describe())

print("\n🔍 EXPERIMENTAL DESIGN:")
print(f"\nConditions:")
print(gene['condition'].value_counts().sort_index())
print(f"\nTimepoints:")
print(gene['timepoint'].value_counts().sort_index())

print("\n🚫 MISSING DATA:")
missing = gene.isnull().sum()
if missing.sum() == 0:
    print("   No missing data!")
else:
    print(missing[missing > 0])

print("\n💡 KEY INSIGHTS:")
print("\nGene expression by condition:")
for condition in gene['condition'].unique():
    subset = gene[gene['condition'] == condition]
    print(f"\n{condition}:")
    print(f"   • Gene A: {subset['gene_A'].mean():.1f} ± {subset['gene_A'].std():.1f}")
    print(f"   • Gene B: {subset['gene_B'].mean():.1f} ± {subset['gene_B'].std():.1f}")
    print(f"   • Gene C: {subset['gene_C'].mean():.1f} ± {subset['gene_C'].std():.1f}")

print("\n\nFold changes (Treated vs Control):")
control_means = gene[gene['condition'] == 'Control'][['gene_A', 'gene_B', 'gene_C']].mean()
treated_means = gene[gene['condition'] == 'Treated'][['gene_A', 'gene_B', 'gene_C']].mean()
fold_changes = treated_means / control_means
for gene_name in ['gene_A', 'gene_B', 'gene_C']:
    fc = fold_changes[gene_name]
    direction = "UP" if fc > 1 else "DOWN"
    print(f"   • {gene_name}: {fc:.2f}x ({direction}regulated)")

print("\n" + "=" * 70)
print("EXPLORATION COMPLETE")
print("=" * 70)
