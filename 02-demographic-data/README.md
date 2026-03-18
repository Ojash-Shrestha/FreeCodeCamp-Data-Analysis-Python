# Demographic Data Analyzer

## Problem
The goal was to analyze a dataset extracted from the 1994 Census database using 
Pandas. The challenge required extracting specific demographic insights, such as 
race representation, education levels, and the relationship between work hours 
and income. The final output needed to be a structured dictionary of statistics, 
with all percentages and averages rounded to the nearest tenth.

## What I built
A Python-based data analysis tool that processes a census CSV file. 
The core logic involves:
- Data filtering: Using boolean indexing to isolate specific subsets, 
  such as filtering for individuals from India or high-earning males.
- Categorical aggregation: Utilizing `.value_counts()` and `.groupby()` 
  to determine distribution across races and countries.
- Advanced metrics: Calculating the percentage of high earners based on 
  education level (Bachelors, Masters, or Doctorate).
- Optimization: Using `.idxmax()` to find the most frequent occupation 
  in a sub-group.

## How to run
```
python main.py
```

## Key concepts learned
- Pandas vectorization: Performing calculations across entire columns without loops
- Data transformation: Using `.isin()` to categorize individuals into groups
- GroupBy aggregation: Using `.groupby()` to calculate statistics per country

## Key findings
- People with higher education are 2.7x more likely to earn >50K
- Iran has the highest percentage of >50K earners at 41.9%
- Only 10% of people working the minimum 1 hour/week earn >50K
- Prof-specialty is the most common occupation among high earners in India

## Output example
```
Number of each race:
 race
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```