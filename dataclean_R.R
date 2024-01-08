# Read the dataset into the 'data' variable
df <- read.csv("drug_overdose_death_rates.csv")
# Check for missing values
str(df)
summary(is.na(df))
# Remove the 'FLAG' column
df<- df[, -which(colnames(df) %in% c("FLAG"))]

library(dplyr)

df <- df %>%
  mutate(
    SEX = case_when(
      grepl("Male", STUB_LABEL) ~ "Male",
      grepl("Female", STUB_LABEL) ~ "Female",
      TRUE ~ NA_character_
    ),
    Hispanic = case_when(
      grepl("Hispanic or Latino: All races", STUB_LABEL) ~ "Hispanic or Latino: All races",
      TRUE ~ NA_character_
    ),
    Non_hispanic = case_when(
      grepl("White", STUB_LABEL) ~ "White",
      grepl("Black or African American", STUB_LABEL) ~ "Black or African American",
      grepl("American Indian or Alaska Native", STUB_LABEL) ~ "American Indian or Alaska Native",
      grepl("Asian or Pacific Islander", STUB_LABEL) ~ "Asian or Pacific Islander",
      TRUE ~ NA_character_
    )
  ) %>%
  filter(!is.na(SEX) | !is.na(Hispanic) | !is.na(Non_hispanic))

write.csv(df, file = "clean_data.csv", row.names = FALSE)