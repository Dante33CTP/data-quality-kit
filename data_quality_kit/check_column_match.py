import pandas as pd

from pandas import DataFrame

def check_column_match(df1: DataFrame, column1: str, df2: DataFrame, column2: str) -> bool:
    """
    Check if all values in column1 of df1 are present in column2 of df2.

    Parameters:
    df1 (DataFrame): The first DataFrame to check.
    column1 (str): The column in the first DataFrame to check for matches.
    df2 (DataFrame): The second DataFrame to check.
    column2 (str): The column in the second DataFrame to check for matches.

    Returns:
    bool: True if all values in column1 of df1 are present in column2 of df2, False otherwise.

    Raises:
    ValueError: If either column does not exist in its respective DataFrame.
    """

    if column1 not in df1.columns:
        #raise ValueError(f'Error: The column "{column1}" does not exist in the first DataFrame.')
        raise ValueError(f'Error: The column "{column1}" not in DataFrame.')
    if column2 not in df2.columns:
        #raise ValueError(f'Error: The column "{column2}" does not exist in the second DataFrame.')
        raise ValueError(f'Error: The column "{column2}" not in DataFrame.')

    return df1[column1].isin(df2[column2]).all()
