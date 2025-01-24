import re

from assertpy import assert_that

from tests.global_test_data import df_global

from data_quality_kit.accuracy import assert_that_type_value, assert_that_values_in_catalog,assert_regex_format


def test_assert_that_type_value_correct():
    assert_that(assert_that_type_value(df_global, 'column1', int)).is_true()
    assert_that(assert_that_type_value(df_global, 'column3', str)).is_true()


def test_assert_that_type_value_incorrect():
    assert_that(assert_that_type_value(df_global, 'column3', int)).is_false()
    assert_that(assert_that_type_value(df_global, 'column2', str)).is_false()


def test_assert_that_type_value_in_nonexistent_column():
    error_msg = 'Column "nonexistent" not in DataFrame.'
    assert_that(assert_that_type_value).raises(ValueError).when_called_with(
        df_global, "nonexistent", int
    ).is_equal_to(error_msg)


def test_assert_that_values_in_catalog_with_all_values_in_catalog():
    catalog = ['Value1', 'Value2', 'Value3', 'Value4']
    result = assert_that_values_in_catalog(df_global, 'test_column', catalog)
    assert_that(result).is_true()


def test_assert_that_values_in_catalog_with_not_all_values_in_catalog():
    catalog = ['Value1', 'Value2', 'Value3']
    result = assert_that_values_in_catalog(df_global, 'test_column', catalog)
    assert_that(result).is_false()


def test_assert_that_values_in_catalog_with_column_not_in_dataframe():
    error_msg = "Column 'non_existent_column' does not exist in the DataFrame."
    assert_that(assert_that_values_in_catalog).raises(ValueError).when_called_with(
        df_global, 'non_existent_column', ['Value1', 'Value2']
    ).is_equal_to(error_msg)


def test_assert_that_values_in_catalog_with_empty_catalog():
    error_msg = "The catalog is empty."
    assert_that(assert_that_values_in_catalog).raises(ValueError).when_called_with(
        df_global, 'test_column', []
    ).is_equal_to(error_msg)

def test_assert_regex_format_with_all_values_matching_pattern():
    regex = r"ES[0-9]{4}"  
    result = assert_regex_format(df_global, 'valid_column', regex)
    assert_that(result).is_equal_to(True)

def test_assert_regex_format_with_some_values_not_matching_pattern():
    regex = r"ES[0-9]{4}"  
    result = assert_regex_format(df_global, 'invalid_column', regex)
    assert_that(result).is_equal_to(False)

def test_assert_regex_format_with_nonexistent_column():
    regex = r"ES[0-9]{4}"  
    assert_that(assert_regex_format).raises(ValueError).when_called_with(
        df_global, 'nonexistent_column', regex
    ).is_equal_to("The column 'nonexistent_column' does not exist in the DataFrame.")

def test_assert_regex_format_with_empty_dataframe():
    empty_df = df_global.iloc[0:0].copy() 
    regex = r"ES[0-9]{4}" 
    assert_that(assert_regex_format).raises(ValueError).when_called_with(
        empty_df, 'regex_test_column', regex
    ).is_equal_to("The DataFrame is empty and cannot be validated.")

def test_assert_regex_format_with_invalid_regex():
    invalid_regex = r"[\K]"
    assert_that(assert_regex_format).raises(ValueError).when_called_with(
        df_global, 'valid_column', invalid_regex
    ).is_equal_to("Invalid regular expression: bad escape \\K at position 1")