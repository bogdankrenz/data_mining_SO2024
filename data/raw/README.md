# Data Description

## Emp

## Exchange Rates

## GDP

## NAICS Occupation

| Field                  | Dtype  | Field Description                        | Redundant |
| ---------------------- | ------ | ---------------------------------------- | :-------: |
| FIPS                   | int    | County identification code               |     N     |
| State_GEOID            | int    | State identification code                |     Y     |
| NAICS                  | object | Industry identification code             |     N     |
| NAICS_TITLE            | object | Industry title                           |     Y     |
| emp_total_county_naics | int    | Total of employees in a county for NAICS |     N     |
| OCC_CODE               | object | Code of occupation title (SOC)           |     N     |
| OCC_TITLE              | object | Occupation description                   |     Y     |
| emp_occupation         | float  | Employees for combination of NAICS & SOC |     N     |

## NAICS Patterns

| Field        | Dtype  | Field Description                                | Redundant |
| ------------ | ------ | ------------------------------------------------ | :-------: |
| State_GEOID  | object | State identification code                        |     Y     |
| County_GEOID | object | County identification code                       |     Y     |
| FIPS         | int    | FIPS code for state & county                     |     N     |
| naics_2      | object | Super NAICS code                                 |     Y     |
| naics        | object | Full NAICS code                                  |     N     |
| DESCRIPTION  | object | NAICS description                                |     Y     |
| emp          | int    | Total "Mid-March" employees                      |     N     |
| qp1          | int    | Total first quarter payroll ($1,000)             |     N     |
| ap           | int    | Total annual payroll ($1,000)                    |     N     |
| est          | int    | Total number of establishments                   |     N     |
| n<5          | object | Number of establishments: <5 Employees           |     N     |
| n5_9         | object | Number of establishments: x Employees            |     N     |
| n10_19       | object | Number of establishments: x Employees            |     N     |
| n20_49       | object | Number of establishments: x Employees            |     N     |
| n50_99       | object | Number of establishments: x Employees            |     N     |
| n100_249     | object | Number of establishments: x Employees            |     N     |
| n250_499     | object | Number of establishments: x Employees            |     N     |
| n500_999     | object | Number of establishments: x Employees            |     N     |
| n1000        | object | Number of establishments: 1000 Employees or more |     N     |
| n1000_1      | object | Number of establishments: 1000 - 1499 Employees  |     N     |
| n1000_2      | object | Number of establishments: 1500 - 2499 Employees  |     N     |
| n1000_3      | object | Number of establishments: 2500 - 4999 Employees  |     N     |
| n1000_4      | object | Number of establishments: 5000 or more Employees |     N     |
| \*\_nf       | object | Noise flag fields                                |     N     |

Maybe we should think of a way to squash the n fields if we want to use them for our project.

## Production Index

## Wages
