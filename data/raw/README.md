# Data Description

## GDP

| Field                  | Field Description               | Redundant |
| ---------------------- | ------------------------------- | :-------: |
| FIPS                   | FIPS codef or state & county    |     N     |
| GeoName                | Name of State or County         |     Y     |
| Region                 |                                 |           |
| TableName              | Irrelevant (only ever "CAGDP9") |     Y     |
| LineCode               |                                 |           |
| IndustryClassification | Industry identification code    |     N     |
| Description            | NAICS description               |     Y     |
| Unit                   | Unit of GDP                     |     Y     |
| 2017 - 2022            | Value of GDP in x Year          |     N     |

## NAICS Occupation

| Field                  | Field Description                        | Redundant |
| ---------------------- | ---------------------------------------- | :-------: |
| FIPS                   | County identification code               |     N     |
| State_GEOID            | State identification code                |     Y     |
| NAICS                  | Industry identification code             |     N     |
| NAICS_TITLE            | Industry title                           |     Y     |
| emp_total_county_naics | Total of employees in a county for NAICS |     N     |
| OCC_CODE               | Code of occupation title (SOC)           |     N     |
| OCC_TITLE              | Occupation description                   |     Y     |
| emp_occupation         | Employees for combination of NAICS & SOC |     N     |

## NAICS Patterns

| Field        | Field Description                                | Redundant |
| ------------ | ------------------------------------------------ | :-------: |
| State_GEOID  | State identification code                        |     Y     |
| County_GEOID | County identification code                       |     Y     |
| FIPS         | FIPS code for state & county                     |     N     |
| naics_2      | Super NAICS code                                 |     Y     |
| naics        | Full NAICS code                                  |     N     |
| DESCRIPTION  | NAICS description                                |     Y     |
| emp          | Total "Mid-March" employees                      |     N     |
| qp1          | Total first quarter payroll ($1,000)             |     N     |
| ap           | Total annual payroll ($1,000)                    |     N     |
| est          | Total number of establishments                   |     N     |
| n<5          | Number of establishments: <5 Employees           |     N     |
| n5_9         | Number of establishments: x Employees            |     N     |
| n10_19       | Number of establishments: x Employees            |     N     |
| n20_49       | Number of establishments: x Employees            |     N     |
| n50_99       | Number of establishments: x Employees            |     N     |
| n100_249     | Number of establishments: x Employees            |     N     |
| n250_499     | Number of establishments: x Employees            |     N     |
| n500_999     | Number of establishments: x Employees            |     N     |
| n1000        | Number of establishments: 1000 Employees or more |     N     |
| n1000_1      | Number of establishments: 1000 - 1499 Employees  |     N     |
| n1000_2      | Number of establishments: 1500 - 2499 Employees  |     N     |
| n1000_3      | Number of establishments: 2500 - 4999 Employees  |     N     |
| n1000_4      | Number of establishments: 5000 or more Employees |     N     |
| x_nf         | Noise flag fields                                |     N     |
