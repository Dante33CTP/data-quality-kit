# Data-Quality-Kit

## Functional Description
A library of functions for managing and improving data quality in Datasets

## Owner
For any bugs or questions, please reach out to [Dante Pedrozo](mailto:dante.victor.33@gmail.com)

## Branching Methodology
This project follows a Git Flow simplified branching methodology
- **Master Branch**: production code
- **Develop Branch**: main integration branch for ongoing development. Features and fixes are merged into this branch before reaching master
- **Feature Branch**: created from develop branch to work on new features

## Prerequisites
This project uses:
- Language: Python 3.10
- Libraries: 
  - pandas
  - pytest
  - assertpy

## How to use it
Install the library

```bash
pip install data-quality-kit
```
```
from data_quality_quick.validate_formats import check_type_format
```

## Functionalities

- **Completeness**
  - **assert_that_dataframe_is_empty**: Check if a DataFrame is empty.
- **Validity**
  - **assert_that_there_are_not_nulls**: Checks for null values in a specified column of a DataFrame.
- **Consistency**
  - **assert_that_there_are_not_duplicates**: Checks for duplicate values in the specified primary key column of a DataFrame.
  - **assert_that_columns_values_match** :  Check if all values in column2 of df2 are present in column1 of df1.
- **Accuracy**
  - **assert_that_type_value**: Check if all non-null entries in a specified column of a DataFrame are of the specified data type.
  - **assert_that_values_in_catalog**:  Checks whether all values in the specified column of a DataFrame are present
    in a catalog (list of values).

