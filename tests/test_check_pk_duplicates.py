import pytest

from assertpy import assert_that

from tests.global_test_data import df_global

from utilities. check_pk_duplicates import check_no_duplicates

def test_no_duplicates():
    assert_that(check_no_duplicates(df_global, 'unique_ids')).is_false()

def test_duplicates():
    assert_that(check_no_duplicates(df_global, 'duplicated_ids')).is_true()

def test_invalid_column_name():
    with pytest.raises(ValueError, match='Error: The column "nonexistent_column" is not in the DataFrame.'):
        check_no_duplicates(df_global, 'nonexistent_column')

