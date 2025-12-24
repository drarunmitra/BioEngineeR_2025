# Project Guidelines for Claude

## Project Overview

This is a biomedical R training and workshop development project. The focus is on creating educational materials for R programming, statistical analysis, and data science in healthcare/biomedical research contexts.

## Workshop Building Context

### Primary Goals
- Create comprehensive R training workshops as Quarto projects
- Develop teaching materials with tidyverse-first approach
- Generate realistic biomedical datasets for instruction
- Build progressive, pedagogically-sound curricula

### Preferred Technologies
- **Document System**: Quarto (books, slides, websites)
- **Presentations**: Reveal.js via Quarto
- **Data Manipulation**: tidyverse (dplyr, tidyr, readr, purrr)
- **Visualization**: ggplot2 with publication themes
- **Tables**: gtsummary, gt, kableExtra
- **Statistical Analysis**: Base R stats, broom for tidy output
- **Reproducibility**: renv for package management

### Teaching Philosophy
1. **Tidyverse-first**: Introduce modern R before base R equivalents
2. **Progressive complexity**: See it → Modify it → Break it → Build it → Extend it
3. **Realistic context**: Use biomedical/health data examples
4. **Active learning**: Hands-on exercises with scaffolded solutions

## Code Style

### R Code Conventions
```r
# Use snake_case for variables and functions
patient_data <- read_csv("data/patients.csv")

# Use native pipe (or magrittr pipe)
result <- data |>
  filter(age >= 18) |>
  group_by(treatment) |>
  summarize(mean_outcome = mean(value, na.rm = TRUE))

# Explicit package prefixes for non-tidyverse functions
janitor::clean_names()
here::here("data", "file.csv")

# Always handle missing data explicitly
mean(x, na.rm = TRUE)
```

### Quarto Document Structure
```
workshop-name/
├── _quarto.yml           # Project configuration
├── index.qmd             # Landing page
├── modules/              # Content chapters
├── slides/               # Reveal.js presentations
├── exercises/            # Hands-on activities
│   ├── */exercise.qmd    # Student version (blanks)
│   └── */solution.qmd    # Instructor version
├── data/                 # Teaching datasets
│   ├── raw/
│   ├── processed/
│   └── data-generation.R
└── _common.R             # Shared setup code
```

### Exercise Format
- Dual versions: participant (with blanks) and instructor (complete)
- Use `___` for fill-in-the-blank code
- Include collapsible hints and solutions
- Show expected output for verification

## Data Guidelines

### Synthetic Data Requirements
- Set seeds for reproducibility
- Use realistic value ranges for biomedical data
- Include intentional missing data patterns
- Create comprehensive codebooks
- Never use or reference real patient data

### Common Variables
- Patient demographics: age (18-95), sex (M/F), race/ethnicity
- Clinical: diagnosis, treatment, BMI, vital signs
- Outcomes: binary (improved/not), continuous scores
- Time: enrollment dates, follow-up periods

## Skills Available

Claude can invoke these skills when relevant:
- `r-workshop-builder`: Build comprehensive R training workshops
- `quarto-teaching`: Create Quarto slides, handouts, exercises
- `quarto-manuscript`: Academic documents with educational elements
- `ggplot-publication`: Publication and teaching visualizations
- `gtsummary-tables`: Summary tables for research and teaching

## Common Tasks

### When Creating Workshop Content
1. Define clear learning objectives
2. Design appropriate synthetic datasets
3. Build modules with progressive complexity
4. Create dual-version exercises
5. Include speaker notes in slides
6. Test all code in fresh R session

### When Building Slides
1. One concept per slide
2. Maximum 12-15 lines of code
3. Use code highlighting for walkthroughs
4. Include speaker notes with timing
5. Mark live coding sections clearly

### When Generating Data
1. Always set seed at script start
2. Document all generation parameters
3. Create codebook with variable definitions
4. Include realistic correlations between variables
5. Add missing data with specified mechanism (MCAR/MAR)

## Output Preferences

- Use Quarto over R Markdown for new content
- Prefer HTML output for development, PDF for distribution
- Include both slides and handout versions
- Always test rendering before committing

## Communication Style

When discussing teaching materials:
- Be explicit about pedagogical choices
- Explain the "why" behind curriculum decisions
- Suggest improvements for learner engagement
- Flag potential confusion points in content
