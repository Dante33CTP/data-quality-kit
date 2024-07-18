import pytest

from assertpy import assert_that

from tests.global_test_data import df_global

from utilities.validate_nulls import check_nulls

def test_nulls_present():
    assert_that(check_nulls(df_global, 'column2')).is_true()

def test_no_nulls():
    assert_that(check_nulls(df_global, 'column1')).is_false()
    assert_that(check_nulls(df_global, 'column3')).is_false()

def test_invalid_column_name():
    with pytest.raises(ValueError, match='Error: The field "nonexistent_column" is not in the DataFrame.'):
        check_nulls(df_global, 'nonexistent_column')

def test_invalid_column_type():
    with pytest.raises(TypeError, match='Error: The field name must be a string.'):
        check_nulls(df_global, 123)

