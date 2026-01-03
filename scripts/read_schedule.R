if (!requireNamespace("readxl", quietly = TRUE)) install.packages("readxl")
library(readxl)
library(here)

path <- here("files/BioEngineeR_2025_Schedule_v2.xlsx")
sheets <- excel_sheets(path)
print(paste("Sheets:", paste(sheets, collapse = ", ")))

for (sheet in sheets) {
    print(paste("--- Sheet:", sheet, "---"))
    data <- read_excel(path, sheet = sheet)
    print(data, n = Inf)
}
