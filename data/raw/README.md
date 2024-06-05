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

## Production Index

## Wages
