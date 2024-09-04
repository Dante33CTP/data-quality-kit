# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.3.0] - 2024-09-04
New functionalities.
### Added
- 
### Changed
- Renamed the function df_is_empty to assert_that_dataframe_is_empty
- Added a new completeness module to the data_quality_kit for enhanced data completeness checks.
- Rename corresponding test cases for the completeness module in the test suite.

### Fixed

## [0.2.0] - 2024-08-03
New functionalities.
### Added
- **check_column_match** : Check if all values in column2 of df2 are present in column1 of df1.
### Changed
- Project aligned to the PEP8 guidelines
### Fixed


## [0.1.0] - 2024-07-21
Base Project Structure.
### Added
- New Module including:
## Functionalities
- **df_is_empty**: Check if a DataFrame is empty.
- **check_nulls**: Checks for null values in a specified column of a DataFrame.
- **check_type_format**: Check if all non-null entries in a specified column of a DataFrame are of the specified data type.
- **check_no_duplicates**: Checks for duplicate values in the specified primary key column of a DataFrame.
### Changed
### Fixed