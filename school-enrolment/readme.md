# Share of children enrolled in pre-primary school - Data package

This data package contains the data that powers the chart ["Share of children enrolled in pre-primary school"](https://ourworldindata.org/grapher/school-enrolment?v=1&csvType=full&useColumnShortNames=false&enrolment_type=net_enrolment&level=preprimary&sex=both) on the Our World in Data website. It was downloaded on May 30, 2026.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For most countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## Net enrollment rate in pre-primary education
Percentage of children of official pre-primary school age who are enrolled in [pre-primary education](#dod:pre-primary-education).
Last updated: May 1, 2025  
Next update: June 2026  
Date range: 1997–2024  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
UNESCO Institute for Statistics (2025) – with minor processing by Our World in Data

#### Full citation
UNESCO Institute for Statistics (2025) – with minor processing by Our World in Data. “Net enrollment rate in pre-primary education” [dataset]. UNESCO Institute for Statistics, “UNESCO Institute for Statistics (UIS) - Education” [original data].
Source: UNESCO Institute for Statistics (2025) – with minor processing by Our World In Data

### What you should know about this data
* The net enrollment rate shows what percentage of children are enrolled at the education level intended for their age.
* It compares children enrolled at the correct level for their age to the total population in that same age group. For example, a primary school net enrollment of 90% means 90% of children between the ages of 6 and 11 years are enrolled in primary school. Children who are not enrolled in school or are enrolled at another education level are not counted here.
* The highest possible value is 100%, which would mean all children of the right age are enrolled where they should be. High rates indicate that most children are progressing through school at the expected pace.
* A rate of 90% doesn't necessarily mean 10% of children are out of school entirely — some may be enrolled at different levels (either higher or lower) than expected for their age, but these students aren't counted in the net rate.
* The data comes from school administrative records that track enrollment by individual age, combined with population estimates from national statistics offices or UN sources.

### Source

#### UNESCO Institute for Statistics – UNESCO Institute for Statistics (UIS) - Education
Retrieved on: 2025-05-01  
Retrieved from: https://databrowser.uis.unesco.org/resources/bulk  


    