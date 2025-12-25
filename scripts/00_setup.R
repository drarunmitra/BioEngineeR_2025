# ============================================
# Workshop Setup Script
# Data Analysis with R | IISc Bio Engineering
# January 6-8, 2025
# ============================================

# Install required packages for the workshop
# Run this script BEFORE the workshop begins

# Core packages
packages <- c(
  # Tidyverse ecosystem
  "tidyverse",    # dplyr, ggplot2, tidyr, readr, etc.

  # Data import
  "readxl",       # Excel files
  "haven",        # SPSS, Stata, SAS
  "here",         # File paths

  # Visualization
  "patchwork",    # Multi-panel figures
  "scales",       # Axis formatting
  "viridis",      # Colorblind-friendly palettes

  # Tables
  "knitr",        # kable tables
  "gt",           # Grammar of tables

  # Statistics
  "broom",        # Tidy model output

  # Reproducibility
  "renv"          # Package management
)

# Install missing packages
install_if_missing <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    message(paste("Installing:", pkg))
    install.packages(pkg, repos = "https://cloud.r-project.org")
  } else {
    message(paste("Already installed:", pkg))
  }
}

# Install all packages
invisible(lapply(packages, install_if_missing))

# Verify installation
message("\n--- Verification ---")
for (pkg in packages) {
  status <- if (requireNamespace(pkg, quietly = TRUE)) "OK" else "FAILED"
  message(paste(pkg, ":", status))
}

message("\nSetup complete! You're ready for the workshop.")
