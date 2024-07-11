import pandas as pd

def check_no_duplicates(df, pk_column) -> str:
    """
    Check if there are no duplicate values in the specified primary key column of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to check.
        pk_column (str): The name of the primary key column to check for duplicates.

    Returns:
        str: 'OK: No duplicate values in the primary key column' if there are no duplicates.

    Raises:
        ValueError: If duplicates are found in the primary key column.
    """
    if pk_column not in df.columns:
        raise ValueError(f'Error: The primary key column "{pk_column}" is not in the DataFrame')
    
    if df[pk_column].duplicated().any():
        raise ValueError(f'KO: Duplicate values found in the primary key column "{pk_column}"')
    return 'OK: No duplicate values in the primary key column'
