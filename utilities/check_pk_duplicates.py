import pandas as pd

def check_no_duplicates(df: pd.DataFrame, pk_column: str) -> bool:
    """
    Check if there are no duplicate values in the specified primary key column of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to check.
        pk_column (str): The name of the primary key column to check for duplicates.

    Returns:
        bool: True if there are no duplicate values in the primary key column and the column exists, False otherwise.
    """
    if pk_column not in df.columns:
        return False
    
    return not df[pk_column].duplicated().any()

