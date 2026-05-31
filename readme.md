# Global Early Childhood Education Trends Analysis

A data analysis project built with Python and Pandas to explore global pre-primary school enrollment trends using education statistics from the UNESCO Institute for Statistics (UIS).

## Overview

This project analyzes pre-primary school enrollment percentages across countries between 1997 and 2024. The goal is to identify trends, measure changes over time, and generate human-readable reports summarizing educational development patterns around the world.

The project automatically processes the dataset, calculates enrollment statistics, evaluates country-level trends, and exports the results as a Markdown report.

## Features

* Analysis of pre-primary school enrollment data across more than 200 countries
* Average enrollment calculations for each country
* Enrollment trend detection using available observations
* Year-to-year change analysis between reported records
* Automatic Markdown report generation
* Data quality and consistency notes

## Technologies Used

* Python
* Pandas
* Markdown

## Dataset Information

Data Source:

* UNESCO Institute for Statistics (UIS)
* Accessed through Our World in Data

Official Sources:

* UNESCO Institute for Statistics (UIS): https://databrowser.uis.unesco.org/
* Our World in Data – Global Education: https://ourworldindata.org/global-education

Dataset Retrieval Date:

* 2025-05-01

## Methodology

For each country, the project:

1. Extracts all available enrollment records.
2. Sorts records chronologically.
3. Calculates the average enrollment percentage.
4. Measures changes between consecutive available observations.
5. Generates a textual summary describing enrollment trends.

## Data Limitations

The dataset contains missing values and irregular reporting intervals for some countries.

As a result:

* Some countries have complete yearly records.
* Some countries contain gaps of several years between observations.
* Reported changes represent differences between available observations and should not always be interpreted as strictly annual changes.

No missing values were artificially generated or estimated by this project.

## Example Output

### Albania

Average enrollment: 64.76%

1999 → 2003: increased by 6.95%

2003 → 2004: decreased by 2.67%

...

## License

### Source Code

This project's source code is released under the MIT License.

### Dataset

The dataset originates from the UNESCO Institute for Statistics (UIS) and remains subject to its original licensing and attribution requirements.

## Attribution

Source: Adapted from UNESCO Institute for Statistics (UIS)

https://databrowser.uis.unesco.org/

Date of extraction: 2025-05-01

## Author

Anas Youssef

GitHub:
https://github.com/mesteranas/

## Educational Purpose

This project was created as a personal learning and portfolio project to develop skills in:

* Data analysis
* Data cleaning
* Statistical reasoning
* Python programming
* Pandas workflows
* Automated report generation
