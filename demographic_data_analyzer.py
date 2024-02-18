import pandas as pd

# Read data from file
  df = pd.read_csv("/adult.data.csv"

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

# What is the average age of men?
  average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

# What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
# percentage with salary >50K
higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)
higher_education_rich


# What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')]
  rich_percentage = num_min_workers = round((rich_work.shape[0] / df[df['hours-per-week'] == min_hours].shape[0]) * 100)

# What country has the highest percentage of people that earn >50K?
# Calculate the count of individuals earning >50K in each country
  count_earning_over_50k_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()

# Calculate the total count of individuals in each country
  total_count_by_country = df['native-country'].value_counts()

# Calculate the percentage of individuals earning >50K in each country
  percentage_earning_over_50k_by_country = (count_earning_over_50k_by_country / total_count_by_country) * 100

# Round the percentages to the nearest tenth
  rounded_percentage_earning_over_50k_by_country = percentage_earning_over_50k_by_country.round(1)

# Find the country with the highest percentage of people earning >50K
  highest_earning_country = rounded_percentage_earning_over_50k_by_country.idxmax()

  highest_earning_country_percentage = rounded_percentage_earning_over_50k_by_country[highest_earning_country]

# Identify the most popular occupation for those who earn >50K in India.
  top_in = demo_data[(demo_data['native-country'] == 'India') & (demo_data['salary'] == '>50K')]
  top_IN_occupation = top_in['occupation'].value_counts().idxmax()


