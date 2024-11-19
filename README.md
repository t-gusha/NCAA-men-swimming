# NCAA-men-swimming

Detailed Description
This project showcases my skills and interests by analyzing NCAA Men's Swimming data. I collected data on the top 16 times in the 100-yard freestyle event at the NCAA Men’s Championships. Currently, the dataset includes years from 2013 to 2024 (excluding 2020 due to COVID). In the future, I plan to expand the dataset to include additional years to improve the reliability of the analysis.

#### The dataset consists of a single entity with the following schema:
```
____________________
|  Place | integer | --> Some 'places' may be shared if two swims have the exact same time.
====================
|  Year  | integer | --> Currently ranges from 2013 to 2024.
====================
| School |  string | 
====================
|  Time  |  float  | --> Each float value has exactly two decimal places, formatted as 'SS.HH'.
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
```
#### This repository contains three Python scripts:
  1. data_validation.py - Ensures the dataset is accurate, consistent, and reliable.
  2. swims_db.py - Defines the database schema using SQLAlchemy.
  3. populate_the_db.py - Extracts data from the Excel file and populates the database.
These scripts use the os, pandas and SQLAlchemy Python libraries. More details about each script can be found in their respective files.

#### This project includes several SQL queries to analyze the data and extract meaningful insights. Below are the queries and their purposes:
  1. Number of Swims by School - Determines how many swims each school has contributed to the top 16.
  2. Difference Between Fastest and Slowest Times by Year - Calculates the time difference between the fastest and slowest swims for each year.
  3. Best Times in the Last 10 Years - Retrieves the best swim times (fastest overall) from the past 10 years.
  4. Average Time per Year - Computes the average swim time for each year in the dataset.
  5. Count of Podium Finishes (1st, 2nd, 3rd) by School - Counts the number of first, second, and third-place finishes for each school.
#### To complement the SQL analysis, I used Tableau to create visualizations of the dataset. These visualizations include:
  1. A bar chart showcasing the number of swims by school.
  2. A line chart highlighting average swim times across years.
  3. A scatter plot showing the fastest vs. slowest times for each year.
  4. A heatmap representing podium finishes (1st, 2nd, and 3rd) by school.

All components of this project are structured into logically named folders within the repository: '/pyCode', '/queries' and '/dataViz'!
#### Improvements
This database has significant potential for expansion. Future improvements could include:
Adding data for other events. Including information about swimmers (e.g., names, ages, and nationalities). Developing automated methods to extract data from sources such as Swimcloud. Currently, I enter data manually by sourcing it from Swimcloud and inputting it into an Excel file. Automating this process would be a valuable enhancement to the project.
