import pandas as pd

def check_nulls(df: pd.DataFrame, field_name: str) -> bool:
    """
    Checks for null values in a specified column of a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to check.
    field_name (str): The name of the column to check for null values.

    Returns:
    bool: True if there are no null values in the column, False if there are any null values.

    Raises:
    TypeError: If the field_name is not a string.
    """
    if not isinstance(field_name, str):
        return False
    
    if field_name not in df.columns:
        return False

    return not df[field_name].isnull().any()
