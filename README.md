

```{r, include=FALSE}
library(caret)
library(mgcv)
library(magrittr)
library(gratia)
library(mlmRev)
library(lme4)
library(rstanarm)
library(ggplot2)
library(kableExtra)
library(tidyverse)
library(ggplot2)
library(tidymodels)
library(recipes)
library(parsnip)
library(workflows)
library(xgboost)
library(yardstick)
library(vip)
library(parsnip)
```

```{r, include=FALSE}

## Using Week 38(oldest) from 2022 and 2023 as Training to predict Week 13 in 2024
week38_2022 <- read.csv("~/Desktop/1st year /703 /Week 14/all-data/2022-week38.csv")
week38_2023 <- read.csv("~/Desktop/1st year /703 /Week 14/all-data/2023-week38.csv")
combined_week38 <- bind_rows(week38_2022, week38_2023)
#combined_week38 <- na.omit(combined_week38)

week13_2024 <- read.csv("~/Desktop/1st year /703 /Week 14/all-data/2024-week13.csv")
#week13_2024 <- na.omit(week13_2024)

```

```{r, include=FALSE}
#recode variables

# Recode variables for 2024
week13_2024$norm_censorship[week13_2024$norm_censorship == "Strongly disagree"] <- 5
week13_2024$norm_censorship[week13_2024$norm_censorship == "Disagree"] <- 4
week13_2024$norm_censorship[week13_2024$norm_censorship == "Neither agree nor disagree"] <- 3
week13_2024$norm_censorship[week13_2024$norm_censorship == "Agree"] <- 2
week13_2024$norm_censorship[week13_2024$norm_censorship == "Strongly agree"] <- 1

week13_2024$norm_judges[week13_2024$norm_judges == "Strongly disagree"] <- 5
week13_2024$norm_judges[week13_2024$norm_judges == "Disagree"] <- 4
week13_2024$norm_judges[week13_2024$norm_judges == "Neither agree nor disagree"] <- 3
week13_2024$norm_judges[week13_2024$norm_judges == "Agree"] <- 2
week13_2024$norm_judges[week13_2024$norm_judges == "Strongly agree"] <- 1

week13_2024$norm_polling[week13_2024$norm_polling == "Strongly disagree"] <- 5
week13_2024$norm_polling[week13_2024$norm_polling == "Disagree"] <- 4
week13_2024$norm_polling[week13_2024$norm_polling == "Neither agree nor disagree"] <- 3
week13_2024$norm_polling[week13_2024$norm_polling == "Agree"] <- 2
week13_2024$norm_polling[week13_2024$norm_polling == "Strongly agree"] <- 1

week13_2024$norm_executive[week13_2024$norm_executive == "Strongly disagree"] <- 5
week13_2024$norm_executive[week13_2024$norm_executive == "Disagree"] <- 4
week13_2024$norm_executive[week13_2024$norm_executive == "Neither agree nor disagree"] <- 3
week13_2024$norm_executive[week13_2024$norm_executive == "Agree"] <- 2
week13_2024$norm_executive[week13_2024$norm_executive == "Strongly agree"] <- 1

week13_2024$norm_loyalty[week13_2024$norm_loyalty == "Strongly disagree"] <- 5
week13_2024$norm_loyalty[week13_2024$norm_loyalty == "Disagree"] <- 4
week13_2024$norm_loyalty[week13_2024$norm_loyalty == "Neither agree nor disagree"] <- 3
week13_2024$norm_loyalty[week13_2024$norm_loyalty == "Agree"] <- 2
week13_2024$norm_loyalty[week13_2024$norm_loyalty == "Strongly agree"] <- 1
week13_2024[, c("norm_censorship", "norm_judges", "norm_polling", "norm_executive", "norm_loyalty")] <- lapply(week13_2024[, c("norm_censorship", "norm_judges", "norm_polling", "norm_executive", "norm_loyalty")], as.numeric)


# Recode variables 2022/2023
combined_week38$norm_censorship[combined_week38$norm_censorship == "Strongly disagree"] <- 5
combined_week38$norm_censorship[combined_week38$norm_censorship == "Disagree"] <- 4
combined_week38$norm_censorship[combined_week38$norm_censorship == "Neither agree nor disagree"] <- 3
combined_week38$norm_censorship[combined_week38$norm_censorship == "Agree"] <- 2
combined_week38$norm_censorship[combined_week38$norm_censorship == "Strongly agree"] <- 1

combined_week38$norm_judges[combined_week38$norm_judges == "Strongly disagree"] <- 5
combined_week38$norm_judges[combined_week38$norm_judges == "Disagree"] <- 4
combined_week38$norm_judges[combined_week38$norm_judges == "Neither agree nor disagree"] <- 3
combined_week38$norm_judges[combined_week38$norm_judges == "Agree"] <- 2
combined_week38$norm_judges[combined_week38$norm_judges == "Strongly agree"] <- 1

combined_week38$norm_polling[combined_week38$norm_polling == "Strongly disagree"] <- 5
combined_week38$norm_polling[combined_week38$norm_polling == "Disagree"] <- 4
combined_week38$norm_polling[combined_week38$norm_polling == "Neither agree nor disagree"] <- 3
combined_week38$norm_polling[combined_week38$norm_polling == "Agree"] <- 2
combined_week38$norm_polling[combined_week38$norm_polling == "Strongly agree"] <- 1

combined_week38$norm_executive[combined_week38$norm_executive == "Strongly disagree"] <- 5
combined_week38$norm_executive[combined_week38$norm_executive == "Disagree"] <- 4
combined_week38$norm_executive[combined_week38$norm_executive == "Neither agree nor disagree"] <- 3
combined_week38$norm_executive[combined_week38$norm_executive == "Agree"] <- 2
combined_week38$norm_executive[combined_week38$norm_executive == "Strongly agree"] <- 1

combined_week38$norm_loyalty[combined_week38$norm_loyalty == "Strongly disagree"] <- 5
combined_week38$norm_loyalty[combined_week38$norm_loyalty == "Disagree"] <- 4
combined_week38$norm_loyalty[combined_week38$norm_loyalty == "Neither agree nor disagree"] <- 3
combined_week38$norm_loyalty[combined_week38$norm_loyalty == "Agree"] <- 2
combined_week38$norm_loyalty[combined_week38$norm_loyalty == "Strongly agree"] <- 1
combined_week38[, c("norm_censorship", "norm_judges", "norm_polling", "norm_executive", "norm_loyalty")] <- lapply(combined_week38[, c("norm_censorship", "norm_judges", "norm_polling", "norm_executive", "norm_loyalty")], as.numeric)

```


```{r, include=FALSE}
combined_week38$violence1[combined_week38$violence1 == "Strongly oppose"] <- 5
combined_week38$violence1[combined_week38$violence1 == "Oppose"] <- 4
combined_week38$violence1[combined_week38$violence1 == "Neither support nor oppose"] <- 3
combined_week38$violence1[combined_week38$violence1 == "Support"] <- 2
combined_week38$violence1[combined_week38$violence1 == "Strongly support"] <- 1

combined_week38$violence2[combined_week38$violence2 == "Strongly oppose"] <- 5
combined_week38$violence2[combined_week38$violence2 == "Oppose"] <- 4
combined_week38$violence2[combined_week38$violence2 == "Neither support nor oppose"] <- 3
combined_week38$violence2[combined_week38$violence2 == "Support"] <- 2
combined_week38$violence2[combined_week38$violence2 == "Strongly support"] <- 1

combined_week38$violence3[combined_week38$violence3 == "Strongly oppose"] <- 5
combined_week38$violence3[combined_week38$violence3 == "Oppose"] <- 4
combined_week38$violence3[combined_week38$violence3 == "Neither support nor oppose"] <- 3
combined_week38$violence3[combined_week38$violence3 == "Support"] <- 2
combined_week38$violence3[combined_week38$violence3 == "Strongly support"] <- 1

combined_week38$violence4[combined_week38$violence4 == "Strongly oppose"] <- 5
combined_week38$violence4[combined_week38$violence4 == "Oppose"] <- 4
combined_week38$violence4[combined_week38$violence4 == "Neither support nor oppose"] <- 3
combined_week38$violence4[combined_week38$violence4 == "Support"] <- 2
combined_week38$violence4[combined_week38$violence4 == "Strongly support"] <- 1

combined_week38$violence5[combined_week38$violence5 == "Strongly oppose"] <- 5
combined_week38$violence5[combined_week38$violence5 == "Oppose"] <- 4
combined_week38$violence5[combined_week38$violence5 == "Neither support nor oppose"] <- 3
combined_week38$violence5[combined_week38$violence5 == "Support"] <- 2
combined_week38$violence5[combined_week38$violence5 == "Strongly support"] <- 1

combined_week38$violence6[combined_week38$violence6 == "Strongly oppose"] <- 5
combined_week38$violence6[combined_week38$violence6 == "Oppose"] <- 4
combined_week38$violence6[combined_week38$violence6 == "Neither support nor oppose"] <- 3
combined_week38$violence6[combined_week38$violence6 == "Support"] <- 2
combined_week38$violence6[combined_week38$violence6 == "Strongly support"] <- 1

combined_week38$gender[combined_week38$gender == "Male"] <- 1
combined_week38$gender[combined_week38$gender == "Female"] <- 2

combined_week38$educ[combined_week38$educ == "No HS"] <- 1
combined_week38$educ[combined_week38$educ == "High school graduate"] <- 2
combined_week38$educ[combined_week38$educ == "Some college"] <- 3
combined_week38$educ[combined_week38$educ == "2-year"] <- 4
combined_week38$educ[combined_week38$educ == "4-year"] <- 5
combined_week38$educ[combined_week38$educ == "Post-grad"] <- 6

combined_week38$faminc_new[combined_week38$faminc_new == "Less than $10000"] <- 1
combined_week38$faminc_new[combined_week38$faminc_new == "$10000 - $19999"] <- 2
combined_week38$faminc_new[combined_week38$faminc_new == "$20000 - $29999"] <- 3
combined_week38$faminc_new[combined_week38$faminc_new == "$30000 - $39999"] <- 4
combined_week38$faminc_new[combined_week38$faminc_new == "$40000 - $49999"] <- 5
combined_week38$faminc_new[combined_week38$faminc_new == "$50000 - $59999"] <- 6
combined_week38$faminc_new[combined_week38$faminc_new == "$60000 - $69999"] <- 7
combined_week38$faminc_new[combined_week38$faminc_new == "$70000 - $79999"] <- 8
combined_week38$faminc_new[combined_week38$faminc_new == "$80000 - $99999"] <- 9
combined_week38$faminc_new[combined_week38$faminc_new == "$100000 - $119999"] <- 10
combined_week38$faminc_new[combined_week38$faminc_new == "$120000 - $149999"] <- 11
combined_week38$faminc_new[combined_week38$faminc_new == "$150000 - $199999"] <- 12
combined_week38$faminc_new[combined_week38$faminc_new == "$200000 - $249999"] <- 13
combined_week38$faminc_new[combined_week38$faminc_new == "$250000 - $349999"] <- 14
combined_week38$faminc_new[combined_week38$faminc_new == "$350000 - $499999"] <- 15
combined_week38$faminc_new[combined_week38$faminc_new == "$500000 or more"] <- 16


combined_week38$votereg[combined_week38$votereg == "No"] <- 0
combined_week38$votereg[combined_week38$votereg == "Yes"] <- 1

combined_week38$general_trust[combined_week38$general_trust == "No"] <- 0
combined_week38$general_trust[combined_week38$general_trust == "Yes"] <- 1

combined_week38$vote_importance[combined_week38$vote_importance == "Very unimportant"] <- 5
combined_week38$vote_importance[combined_week38$vote_importance == "Unimportant"] <- 4
combined_week38$vote_importance[combined_week38$vote_importance == "Neither important nor unimportant"] <- 3
combined_week38$vote_importance[combined_week38$vote_importance == "Important"] <- 2
combined_week38$vote_importance[combined_week38$vote_importance == "Very important"] <- 1

combined_week38$fair_treatment[combined_week38$fair_treatment == "Strongly disagree"] <- 5
combined_week38$fair_treatment[combined_week38$fair_treatment == "Disagree"] <- 4
combined_week38$fair_treatment[combined_week38$fair_treatment == "Neither agree nor disagree"] <- 3
combined_week38$fair_treatment[combined_week38$fair_treatment == "Agree"] <- 2
combined_week38$fair_treatment[combined_week38$fair_treatment == "Strongly agree"] <- 1

combined_week38$race[combined_week38$race == "White"] <- 1
combined_week38$race[combined_week38$race == "Black"] <- 0
combined_week38$race[combined_week38$race == "Hispanic"] <- 0
combined_week38$race[combined_week38$race == "Asian"] <- 0
combined_week38$race[combined_week38$race == "Native American"] <- 0
combined_week38$race[combined_week38$race == "Two or more races"] <- 0
combined_week38$race[combined_week38$race == "Other"] <- 0
combined_week38$race[combined_week38$race == "Middle Eastern"] <- 0

combined_week38$marstat[combined_week38$marstat == "Married"] <- 1
combined_week38$marstat[combined_week38$marstat == "Separated"] <- 0
combined_week38$marstat[combined_week38$marstat == "Divorced"] <- 0
combined_week38$marstat[combined_week38$marstat == "Widowed"] <- 0
combined_week38$marstat[combined_week38$marstat == "Never married"] <- 0
combined_week38$marstat[combined_week38$marstat == "Domestic / civil partnership"] <- 0

combined_week38$employ[combined_week38$employ == "Full-time"] <- 1
combined_week38$employ[combined_week38$employ == "Part-time"] <- 1
combined_week38$employ[combined_week38$employ == "Temporarily laid off"] <- 0
combined_week38$employ[combined_week38$employ == "Unemployed"] <- 0
combined_week38$employ[combined_week38$employ == "Retired"] <- 0
combined_week38$employ[combined_week38$employ == "Permanently disabled"] <- 0
combined_week38$employ[combined_week38$employ == "Homemaker"] <- 0
combined_week38$employ[combined_week38$employ == "Student"] <- 0
combined_week38$employ[combined_week38$employ == "Other"] <- 0

combined_week38$child18[combined_week38$child18 == "No"] <- 0
combined_week38$child18[combined_week38$child18 == "Yes"] <- 1

combined_week38$pid3[combined_week38$pid3 == "Independent"] <- 0
combined_week38$pid3[combined_week38$pid3 == "Republican"] <- 0
combined_week38$pid3[combined_week38$pid3 == "Democrat"] <- 1

combined_week38$affective_polarization <- abs(combined_week38$democrat_therm_1 - combined_week38$republican_therm_1)

combined_week38$pride[combined_week38$pride == "Not at all proud"] <- 1
combined_week38$pride[combined_week38$pride == "Only a little proud"] <- 2
combined_week38$pride[combined_week38$pride == "Moderately proud"] <- 3
combined_week38$pride[combined_week38$pride == "Very proud"] <- 4
combined_week38$pride[combined_week38$pride == "Extremely proud"] <- 5

combined_week38$maga[combined_week38$maga == "MAGA Republican"] <- 1
combined_week38$maga[combined_week38$maga == "Never Trumper"] <- 0
combined_week38$maga[combined_week38$maga == "Neither"] <- 0


combined_week38[, c("democrat_therm_1", "republican_therm_1", "general_trust", "vote_importance", "fair_treatment", "race", "marstat", "faminc_new", "educ", "gender", "violence6", "violence5", "violence4", "violence3", "violence2", "violence1", "employ", "pid3", "child18", "affective_polarization", "pride", "maga")] <- lapply(combined_week38[, c("democrat_therm_1", "republican_therm_1", "general_trust", "vote_importance", "fair_treatment", "race", "marstat", "faminc_new", "educ", "gender", "violence6", "violence5", "violence4", "violence3", "violence2", "violence1", "employ", "pid3", "child18", "affective_polarization", "pride", "maga")], as.numeric)


```

```{r, include=FALSE}
week13_2024$violence1[week13_2024$violence1 == "Strongly oppose"] <- 5
week13_2024$violence1[week13_2024$violence1 == "Oppose"] <- 4
week13_2024$violence1[week13_2024$violence1 == "Neither support nor oppose"] <- 3
week13_2024$violence1[week13_2024$violence1 == "Support"] <- 2
week13_2024$violence1[week13_2024$violence1 == "Strongly support"] <- 1


week13_2024$violence2[week13_2024$violence2 == "Strongly oppose"] <- 5
week13_2024$violence2[week13_2024$violence2 == "Oppose"] <- 4
week13_2024$violence2[week13_2024$violence2 == "Neither support nor oppose"] <- 3
week13_2024$violence2[week13_2024$violence2 == "Support"] <- 2
week13_2024$violence2[week13_2024$violence2 == "Strongly support"] <- 1

week13_2024$violence3[week13_2024$violence3 == "Strongly oppose"] <- 5
week13_2024$violence3[week13_2024$violence3 == "Oppose"] <- 4
week13_2024$violence3[week13_2024$violence3 == "Neither support nor oppose"] <- 3
week13_2024$violence3[week13_2024$violence3 == "Support"] <- 2
week13_2024$violence3[week13_2024$violence3 == "Strongly support"] <- 1

week13_2024$violence4[week13_2024$violence4 == "Strongly oppose"] <- 5
week13_2024$violence4[week13_2024$violence4 == "Oppose"] <- 4
week13_2024$violence4[week13_2024$violence4 == "Neither support nor oppose"] <- 3
week13_2024$violence4[week13_2024$violence4 == "Support"] <- 2
week13_2024$violence4[week13_2024$violence4 == "Strongly support"] <- 1

week13_2024$violence5[week13_2024$violence5 == "Strongly oppose"] <- 5
week13_2024$violence5[week13_2024$violence5 == "Oppose"] <- 4
week13_2024$violence5[week13_2024$violence5 == "Neither support nor oppose"] <- 3
week13_2024$violence5[week13_2024$violence5 == "Support"] <- 2
week13_2024$violence5[week13_2024$violence5 == "Strongly support"] <- 1

week13_2024$violence6[week13_2024$violence6 == "Strongly oppose"] <- 5
week13_2024$violence6[week13_2024$violence6 == "Oppose"] <- 4
week13_2024$violence6[week13_2024$violence6 == "Neither support nor oppose"] <- 3
week13_2024$violence6[week13_2024$violence6 == "Support"] <- 2
week13_2024$violence6[week13_2024$violence6 == "Strongly support"] <- 1

week13_2024$gender[week13_2024$gender == "Male"] <- 1
week13_2024$gender[week13_2024$gender == "Female"] <- 2

week13_2024$educ[week13_2024$educ == "No HS"] <- 1
week13_2024$educ[week13_2024$educ == "High school graduate"] <- 2
week13_2024$educ[week13_2024$educ == "Some college"] <- 3
week13_2024$educ[week13_2024$educ == "2-year"] <- 4
week13_2024$educ[week13_2024$educ == "4-year"] <- 5
week13_2024$educ[week13_2024$educ == "Post-grad"] <- 6

week13_2024$faminc_new[week13_2024$faminc_new == "Less than $10000"] <- 1
week13_2024$faminc_new[week13_2024$faminc_new == "$10000 - $19999"] <- 2
week13_2024$faminc_new[week13_2024$faminc_new == "$20000 - $29999"] <- 3
week13_2024$faminc_new[week13_2024$faminc_new == "$30000 - $39999"] <- 4
week13_2024$faminc_new[week13_2024$faminc_new == "$40000 - $49999"] <- 5
week13_2024$faminc_new[week13_2024$faminc_new == "$50000 - $59999"] <- 6
week13_2024$faminc_new[week13_2024$faminc_new == "$60000 - $69999"] <- 7
week13_2024$faminc_new[week13_2024$faminc_new == "$70000 - $79999"] <- 8
week13_2024$faminc_new[week13_2024$faminc_new == "$80000 - $99999"] <- 9
week13_2024$faminc_new[week13_2024$faminc_new == "$100000 - $119999"] <- 10
week13_2024$faminc_new[week13_2024$faminc_new == "$120000 - $149999"] <- 11
week13_2024$faminc_new[week13_2024$faminc_new == "$150000 - $199999"] <- 12
week13_2024$faminc_new[week13_2024$faminc_new == "$200000 - $249999"] <- 13
week13_2024$faminc_new[week13_2024$faminc_new == "$250000 - $349999"] <- 14
week13_2024$faminc_new[week13_2024$faminc_new == "$350000 - $499999"] <- 15
week13_2024$faminc_new[week13_2024$faminc_new == "$500000 or more"] <- 16

week13_2024$votereg[week13_2024$votereg == "No"] <- 0
week13_2024$votereg[week13_2024$votereg == "Yes"] <- 1


week13_2024$general_trust[week13_2024$general_trust == "No"] <- 0
week13_2024$general_trust[week13_2024$general_trust == "Yes"] <- 1


week13_2024$vote_importance[week13_2024$vote_importance == "Very unimportant
"] <- 5
week13_2024$vote_importance[week13_2024$vote_importance == "Unimportant"] <- 4
week13_2024$vote_importance[week13_2024$vote_importance == "Neither important nor unimportant"] <- 3
week13_2024$vote_importance[week13_2024$vote_importance == "Important"] <- 2
week13_2024$vote_importance[week13_2024$vote_importance == "Very important"] <- 1

week13_2024$fair_treatment[week13_2024$fair_treatment == "Strongly disagree"] <- 5
week13_2024$fair_treatment[week13_2024$fair_treatment == "Disagree"] <- 4
week13_2024$fair_treatment[week13_2024$fair_treatment == "Neither agree nor disagree"] <- 3
week13_2024$fair_treatment[week13_2024$fair_treatment == "Agree"] <- 2
week13_2024$fair_treatment[week13_2024$fair_treatment == "Strongly agree"] <- 1

week13_2024$race[week13_2024$race == "White"] <- 1
week13_2024$race[week13_2024$race == "Black"] <- 0
week13_2024$race[week13_2024$race == "Hispanic"] <- 0
week13_2024$race[week13_2024$race == "Asian"] <- 0
week13_2024$race[week13_2024$race == "Native American"] <- 0
week13_2024$race[week13_2024$race == "Two or more races"] <- 0
week13_2024$race[week13_2024$race == "Other"] <- 0
week13_2024$race[week13_2024$race == "Middle Eastern"] <- 0


week13_2024$marstat[week13_2024$marstat == "Married"] <- 1
week13_2024$marstat[week13_2024$marstat == "Separated"] <- 0
week13_2024$marstat[week13_2024$marstat == "Divorced"] <- 0
week13_2024$marstat[week13_2024$marstat == "Widowed"] <- 0
week13_2024$marstat[week13_2024$marstat == "Never married"] <- 0
week13_2024$marstat[week13_2024$marstat == "Domestic / civil partnership"] <- 0

week13_2024$employ[week13_2024$employ == "Full-time"] <- 1
week13_2024$employ[week13_2024$employ == "Part-time"] <- 1
week13_2024$employ[week13_2024$employ == "Temporarily laid off"] <- 0
week13_2024$employ[week13_2024$employ == "Unemployed"] <- 0
week13_2024$employ[week13_2024$employ == "Retired"] <- 0
week13_2024$employ[week13_2024$employ == "Permanently disabled"] <- 0
week13_2024$employ[week13_2024$employ == "Homemaker"] <- 0
week13_2024$employ[week13_2024$employ == "Student"] <- 0
week13_2024$employ[week13_2024$employ == "Other"] <- 0

week13_2024$child18[week13_2024$child18 == "No"] <- 0
week13_2024$child18[week13_2024$child18 == "Yes"] <- 1



week13_2024$pid3[week13_2024$pid3 == "Independent/Other"] <- 0
week13_2024$pid3[week13_2024$pid3 == "Republican"] <- 0
week13_2024$pid3[week13_2024$pid == "Democrat"] <- 1

week13_2024$affective_polarization <- abs(week13_2024$democrat_therm_1 - week13_2024$republican_therm_1)

week13_2024$pride[week13_2024$pride == "Not at all proud"] <- 1
week13_2024$pride[week13_2024$pride == "Only a little proud"] <- 2
week13_2024$pride[week13_2024$pride == "Moderately proud"] <- 3
week13_2024$pride[week13_2024$pride == "Very proud"] <- 4
week13_2024$pride[week13_2024$pride == "Extremely proud"] <- 5

week13_2024$maga[week13_2024$maga == "MAGA Republican"] <- 1
week13_2024$maga[week13_2024$maga == "Never Trumper"] <- 0
week13_2024$maga[week13_2024$maga == "Neither"] <- 0

week13_2024[, c("democrat_therm_1","republican_therm_1","general_trust", "vote_importance","fair_treatment","race","marstat", "faminc_new", "educ", "gender", "violence6", "violence5", "violence4", "violence3", "violence2", "violence1","employ", "pid3", "child18", "affective_polarization", "pride", "maga")] <- lapply(week13_2024[, c("democrat_therm_1","republican_therm_1", "general_trust","vote_importance","fair_treatment", "race", "marstat", "faminc_new", "educ", "gender", "violence6", "violence5", "violence4", "violence3", "violence2", "violence1", "employ", "pid3", "child18", "affective_polarization", "pride", "maga")], as.numeric)

```

```{r, include=FALSE}
#Creating Norm index- agree with statments, less democratic norms support - 5 indicates opposture and more support of norms

week13_2024$democratic_norms <- (week13_2024$norm_censorship + week13_2024$norm_judges + week13_2024$norm_polling + week13_2024$norm_executive + week13_2024$norm_loyalty) / 5



combined_week38$democratic_norms <- (combined_week38$norm_censorship + combined_week38$norm_judges + combined_week38$norm_polling + combined_week38$norm_executive + combined_week38$norm_loyalty) / 5

```


 
```{r, include=FALSE}
##Recipe
#summary(week13_2024)
#recipe <- recipe(democratic_norms ~general_trust + institutional_corruption+ vote_importance+ pride + fair_treatment+violence3_perception +violence6_perception + )

recipe_combind <- recipe(democratic_norms ~ democrat_therm_1 + republican_therm_1 + general_trust + vote_importance + fair_treatment + race + marstat + educ + gender + violence6 + violence5 + violence4 + violence3 
                         + violence2 + violence1 + employ + pid3 + child18 + affective_polarization + pride + maga
, data = combined_week38) %>%
    step_normalize(all_predictors(), -all_outcomes())


boost_tree_spec <- boost_tree(
  mode = "regression", 
  trees = 1000, 
  tree_depth = 3,
  min_n = 10,
  loss_reduction = 0.01, 
  sample_size = 0.5, 
  mtry = 2, 
  learn_rate = 0.01, 
  engine = "xgboost"
)



boosting_workflow <- workflow() %>%
  add_recipe(recipe_combind) %>%
  add_model(boost_tree_spec)


fit <- boosting_workflow %>%
  fit(data = combined_week38)


fit %>%
  extract_fit_parsnip() %>%
  vip()

fit %>%
  fit(data = combined_week38) %>%
  extract_fit_parsnip() %>%
  vip(geom = "point")



```





# Introduction
In today's political landscape, understanding individuals' attitudes towards democratic norms is crucial for assessing the health of democratic systems and predicting threats to democratic governance. Antidemocratic attitudes, characterized by skepticism or outright rejection of democratic principles, can undermine the functioning of democratic institutions and processes. Therefore, identifying the factors that predict such attitudes is of paramount importance.

Although, in most cases, it may be unclear where to start. Furthermore, which variables are important to include in our models. 

To overcome this uncertainty, this lab takes the first steps in investigating and laying out important variables., I utilize data from The American Political Pulse by creating a combined data set of the information from week 38 in 2020 and 2023. With this combined data set, I seek to predict attitudes towards democratic norms in the most recent data collected closest in time (Week 13)

Overall, this laboratory exercise serves as a important and clarifying step towards enhancing our understanding of individuals' attitudes towards democratic norms and provides valuable insights into possible factors that could have a role in antidemocratic sentiments in contemporary societies.
 
## Democratic Norms
To measure individuals' attitudes towards democratic norms, i created an index containing five different variables. Each variable asks whether respondents agree or disagree with certain scenarios. The coding scheme assigns a score of 5 to respondents who strongly disagree, indicating support for democratic norms.

The first variable assesses respondents' views on whether judges should ignore decisions issued by presidents of the outparty. The second variable gauges their support for reducing polling stations in regions known for the outparty. The third variable questions the justification of presidents using power to advance their own priorities when they cannot secure cooperation from the outparty. The fourth variable inquires about reducing media attacks on the inparty. Lastly, the fifth variable asks respondents about their stance on candidates prioritizing party loyalty over adherence to rules and the constitution. These variables are combined to create an index ranging from 1 to 5. A score of 5 indicates strong support for democratic norms, while a score of 1 suggests little to no support for democratic norms.

## Method

To assess the importance of variables, I will utilize a machine learning model employing gradient boosting. This method is particularly suitable for this investigation due to its ability to handle complex models effectively. The model will incorporate 25 variables, allowing me to identify the most influential variables in predicting attitudes towards democratic norms.

Additionally, this approach offers advantages such as accurate predictions and the ability to handle nonlinearity and interactions as needed.


### Important Variables

Below is the plot demonstrating which variables appear to be important. Variables that appear to be important in regards to democratic norms include the Republican thermometer, violence 2, violence 1, democratic thermometer, and violence 3.

Future steps could include utilizing the violence variables and possibly creating an index to encompass all of them. The relationship between individual perceptions of violence should be investigated further to determine if there is a relationship between them and democratic norms.

```{r, echo=FALSE}

fit %>% 
  extract_fit_parsnip() %>% 
  vip(num_features = 25, include_type = TRUE) +
  ggtitle("Variable Importance") 
```


### Predictions

Another advantage of this method is its ability to make accurate predictions. The table provides the statistics necessary to evaluate the overall performance of the model. The RMSE indicates how far off predictions were from the actual values. We generally want small numbers indicating that they are close to the points. 0.747 is larger than we would hope. RSQ is just R2; this model explains 28% of the variation in the data, which is not the best. MAE is the median absolute error and it is similar to RSQ, just not as sensitive to outliers.

Below is a plot displaying the model's predictions compared to the actual values. Ideally, we would observe a positive slope, indicating that when the actual value of democratic norms is 1, the prediction is also 1. However, we notice that the data is sparse at the beginning of the plot. When the actual value of democratic norms is between 1 and 2, there is a larger variance or spread in predictions by the model. However, once the values exceed 2, the spread begins to tighten.


```{r, echo=FALSE}
predictions <- predict(fit, new_data = week13_2024)
predicted_values <- predictions$.pred


predicted_probabilities <- predict(fit, new_data = week13_2024) # For binary data maby?

actual_vs_predicted <- week13_2024 %>%
  select(democratic_norms) %>%
  bind_cols(predicted_probabilities)


boost_metrics_small <- actual_vs_predicted %>%
  metrics(truth = democratic_norms, estimate = .pred)%>%
  kable(format = "markdown", col.names = c("Metric", "Estimator", "Estimate")) %>%
  kable_styling()


boost_metrics_small





```

```{r, echo= FALSE}
library(ggplot2)
p <- ggplot(actual_vs_predicted, aes(x = democratic_norms, y = .pred, colour = democratic_norms))
p + geom_point() +
    labs(x = "Democratic Norms", y = "Predicted Values", title = "Scatterplot of Predicted vs Actual Values") 
```

## Conclusion


The results of this assessment suggest that future research on democratic norms should prioritize variables measuring perceptions of violence, as well as polarization measures. Support for violence is found to be important for understanding democratic norms possible due to its connection to moral judgments. Support for violence often reflects individuals' moral judgments regarding the use of force or coercion to achieve political goals. In a democratic society, peaceful and nonviolent means of expressing dissent and effecting change are typically valued. Democratic norms encompass a set of values, principles, and behaviors that connect to democratic governance, such as respect for the rule of law, protection of individual rights, and adherence to peaceful conflict resolution mechanisms. The significance of support for violence as an important variable in measuring support for democratic norms lies in its reflection of individuals' moral judgments, attitudes towards democratic principles, and potential implications for democratic governance and stability. High levels of polarization may indicate a breakdown in these democratic principles, as individuals become entrenched in their positions and view political opponents as adversaries rather than fellow citizens.

In summary, future research leveraging variables related to perceptions of violence and political polarization in predictive models offers a promising avenue for advancing our understanding of democratic norms.

