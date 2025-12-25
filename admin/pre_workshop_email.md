# Pre-Workshop Email Template

---

**Subject:** Data Analysis with R Workshop - Pre-Workshop Instructions

---

Dear Participant,

Welcome to the **Data Analysis with R** workshop at IISc Bio Engineering!

**Workshop Details:**
- **Dates:** January 6-8, 2025
- **Time:** 9:00 AM - 5:00 PM daily
- **Venue:** [Room/Building Name]

## Before the Workshop

Please complete the following setup **before** arriving:

### 1. Install R
Download from: https://cran.r-project.org/
- Windows: Click "Download R for Windows" → "base" → Download
- Mac: Click "Download R for macOS" → Select appropriate version
- Linux: Follow instructions for your distribution

### 2. Install RStudio
Download from: https://posit.co/download/rstudio-desktop/
- Select the free "RStudio Desktop" version
- Choose your operating system

### 3. Install Required Packages
Open RStudio and run:

```r
install.packages(c("tidyverse", "here", "readxl", "patchwork", "broom", "knitr"))
```

### 4. Verify Installation
Run this code to verify everything works:

```r
library(tidyverse)
ggplot(mtcars, aes(x = wt, y = mpg)) + geom_point()
```

You should see a scatter plot appear.

## What to Bring

- Laptop with R and RStudio installed
- Laptop charger
- Your own data (optional, for Day 2 practice session)
- Questions about R or your research!

## Need Help?

If you encounter installation issues, please email [instructor@email.com] before the workshop.

We look forward to seeing you!

Best regards,
[Instructor Name]
Workshop Instructor
