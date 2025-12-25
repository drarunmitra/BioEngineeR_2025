# Common R Setup for IISc R Workshop 2025
suppressPackageStartupMessages({
  library(tidyverse)
  library(here)
})

theme_set(theme_classic(base_size = 12))

# Publication theme
theme_publication <- function(base_size = 12) {
  theme_classic(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", hjust = 0),
      axis.title = element_text(face = "bold"),
      legend.position = "bottom",
      panel.border = element_rect(fill = NA, color = "black")
    )
}

# Colorblind-safe palette
okabe_ito <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442",
               "#0072B2", "#D55E00", "#CC79A7", "#999999")

set.seed(2025)
