#!/usr/bin/env python3
"""
Visualize Generated Datasets
Data Analysis with R | IISc Bio Engineering
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)

# Create output directory
output_dir = Path('/home/user/BioEngineeR_2026/figures')
output_dir.mkdir(exist_ok=True)

# ============================================
# Dataset 1: Clinical Trial Visualizations
# ============================================

clinical = pd.read_csv('/home/user/BioEngineeR_2026/data/clinical_trial.csv')

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Clinical Trial Dataset - Exploratory Analysis', fontsize=16, fontweight='bold')

# Age distribution
axes[0, 0].hist(clinical['age'], bins=15, color='steelblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Age (years)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].axvline(clinical['age'].mean(), color='red', linestyle='--', label=f'Mean: {clinical["age"].mean():.1f}')
axes[0, 0].legend()

# BMI distribution
axes[0, 1].hist(clinical['bmi'], bins=15, color='coral', edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('BMI')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('BMI Distribution')
axes[0, 1].axvline(clinical['bmi'].mean(), color='red', linestyle='--', label=f'Mean: {clinical["bmi"].mean():.1f}')
axes[0, 1].legend()

# Treatment distribution
treatment_counts = clinical['treatment'].value_counts()
axes[0, 2].bar(treatment_counts.index, treatment_counts.values, color=['lightblue', 'lightgreen', 'salmon'])
axes[0, 2].set_xlabel('Treatment Group')
axes[0, 2].set_ylabel('Count')
axes[0, 2].set_title('Treatment Group Distribution')
axes[0, 2].tick_params(axis='x', rotation=45)

# Change score by treatment
treatment_order = ['Placebo', 'Low Dose', 'High Dose']
clinical['treatment'] = pd.Categorical(clinical['treatment'], categories=treatment_order, ordered=True)
axes[1, 0].boxplot([clinical[clinical['treatment'] == t]['change_score'] for t in treatment_order],
                    labels=treatment_order)
axes[1, 0].set_xlabel('Treatment Group')
axes[1, 0].set_ylabel('Change Score')
axes[1, 0].set_title('Treatment Effect on Change Score')
axes[1, 0].axhline(0, color='gray', linestyle='--', alpha=0.5)
axes[1, 0].tick_params(axis='x', rotation=45)

# Responder rate by treatment
responder_rate = clinical.groupby('treatment')['responder'].mean() * 100
axes[1, 1].bar(responder_rate.index, responder_rate.values, color=['lightblue', 'lightgreen', 'salmon'])
axes[1, 1].set_xlabel('Treatment Group')
axes[1, 1].set_ylabel('Responder Rate (%)')
axes[1, 1].set_title('Responder Rate by Treatment')
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].axhline(50, color='gray', linestyle='--', alpha=0.5)

# Baseline vs Week 8 scores
axes[1, 2].scatter(clinical['baseline_score'], clinical['week_8_score'],
                   c=pd.Categorical(clinical['treatment']).codes, cmap='Set2', alpha=0.6, s=50)
axes[1, 2].plot([0, 100], [0, 100], 'k--', alpha=0.3, label='No change')
axes[1, 2].set_xlabel('Baseline Score')
axes[1, 2].set_ylabel('Week 8 Score')
axes[1, 2].set_title('Baseline vs Week 8 Scores')
axes[1, 2].legend(['No change', 'Patients'])

plt.tight_layout()
plt.savefig(output_dir / 'clinical_trial_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Saved: figures/clinical_trial_analysis.png")

# ============================================
# Dataset 2: Cell Viability Visualizations
# ============================================

cell = pd.read_csv('/home/user/BioEngineeR_2026/data/cell_viability.csv')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Cell Viability Study - Exploratory Analysis', fontsize=16, fontweight='bold')

# Viability by treatment
treatment_order = ['Control', 'Drug_A', 'Drug_B', 'Combo']
cell['treatment'] = pd.Categorical(cell['treatment'], categories=treatment_order, ordered=True)
axes[0, 0].boxplot([cell[cell['treatment'] == t]['viability'] for t in treatment_order],
                    labels=treatment_order)
axes[0, 0].set_xlabel('Treatment')
axes[0, 0].set_ylabel('Viability (%)')
axes[0, 0].set_title('Cell Viability by Treatment')
axes[0, 0].tick_params(axis='x', rotation=45)

# Apoptosis by treatment
axes[0, 1].boxplot([cell[cell['treatment'] == t]['apoptosis'] for t in treatment_order],
                    labels=treatment_order)
axes[0, 1].set_xlabel('Treatment')
axes[0, 1].set_ylabel('Apoptosis (%)')
axes[0, 1].set_title('Apoptosis by Treatment')
axes[0, 1].tick_params(axis='x', rotation=45)

# Viability by cell line
cell_lines = ['HeLa', 'MCF7', 'A549']
axes[1, 0].boxplot([cell[cell['cell_line'] == cl]['viability'] for cl in cell_lines],
                    labels=cell_lines)
axes[1, 0].set_xlabel('Cell Line')
axes[1, 0].set_ylabel('Viability (%)')
axes[1, 0].set_title('Viability by Cell Line')

# Viability vs Apoptosis
for treatment in treatment_order:
    subset = cell[cell['treatment'] == treatment]
    axes[1, 1].scatter(subset['viability'], subset['apoptosis'],
                      label=treatment, alpha=0.6, s=50)
axes[1, 1].set_xlabel('Viability (%)')
axes[1, 1].set_ylabel('Apoptosis (%)')
axes[1, 1].set_title('Viability vs Apoptosis')
axes[1, 1].legend()
axes[1, 1].plot([0, 100], [100, 0], 'k--', alpha=0.3, linewidth=1)

plt.tight_layout()
plt.savefig(output_dir / 'cell_viability_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Saved: figures/cell_viability_analysis.png")

# ============================================
# Dataset 3: Gene Expression Visualizations
# ============================================

gene = pd.read_csv('/home/user/BioEngineeR_2026/data/gene_expression.csv')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Gene Expression Study - Exploratory Analysis', fontsize=16, fontweight='bold')

# Gene A expression
gene_a_data = [gene[gene['condition'] == c]['gene_A'] for c in ['Control', 'Treated']]
axes[0, 0].boxplot(gene_a_data, labels=['Control', 'Treated'])
axes[0, 0].set_ylabel('Expression Level')
axes[0, 0].set_title('Gene A Expression (Upregulated)')
axes[0, 0].text(0.5, 0.95, '↑ 1.74x', transform=axes[0, 0].transAxes,
               fontsize=14, color='red', fontweight='bold', ha='center')

# Gene B expression
gene_b_data = [gene[gene['condition'] == c]['gene_B'] for c in ['Control', 'Treated']]
axes[0, 1].boxplot(gene_b_data, labels=['Control', 'Treated'])
axes[0, 1].set_ylabel('Expression Level')
axes[0, 1].set_title('Gene B Expression (Downregulated)')
axes[0, 1].text(0.5, 0.95, '↓ 0.67x', transform=axes[0, 1].transAxes,
               fontsize=14, color='blue', fontweight='bold', ha='center')

# Gene C expression
gene_c_data = [gene[gene['condition'] == c]['gene_C'] for c in ['Control', 'Treated']]
axes[1, 0].boxplot(gene_c_data, labels=['Control', 'Treated'])
axes[1, 0].set_ylabel('Expression Level')
axes[1, 0].set_title('Gene C Expression (Slightly upregulated)')
axes[1, 0].text(0.5, 0.95, '↑ 1.09x', transform=axes[1, 0].transAxes,
               fontsize=14, color='orange', fontweight='bold', ha='center')

# Expression by timepoint
timepoint_order = ['0h', '6h', '24h']
gene['timepoint'] = pd.Categorical(gene['timepoint'], categories=timepoint_order, ordered=True)
mean_expr = gene.groupby(['condition', 'timepoint'])[['gene_A', 'gene_B', 'gene_C']].mean()

x = range(len(timepoint_order))
width = 0.35
x_control = [i - width/2 for i in x]
x_treated = [i + width/2 for i in x]

for gene_name, color in [('gene_A', 'red'), ('gene_B', 'blue'), ('gene_C', 'green')]:
    axes[1, 1].plot(x_control,
                   [mean_expr.loc[('Control', tp), gene_name] for tp in timepoint_order],
                   'o-', color=color, alpha=0.6, label=f'{gene_name} Control')
    axes[1, 1].plot(x_treated,
                   [mean_expr.loc[('Treated', tp), gene_name] for tp in timepoint_order],
                   's-', color=color, label=f'{gene_name} Treated')

axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(timepoint_order)
axes[1, 1].set_xlabel('Timepoint')
axes[1, 1].set_ylabel('Mean Expression Level')
axes[1, 1].set_title('Gene Expression Over Time')
axes[1, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)

plt.tight_layout()
plt.savefig(output_dir / 'gene_expression_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Saved: figures/gene_expression_analysis.png")

print("\n✨ All visualizations complete!")
print(f"   Saved to: {output_dir}/")
