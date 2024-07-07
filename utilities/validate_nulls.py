from pandas import DataFrame

def check_nulls(df: DataFrame, field_name: str) -> str:
    """
    Checks for null values in a specified column of a DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to check.
    field_name (str): The name of the column to check for null values.

    Returns:
    str: 'KO' if there are any null values in the column, otherwise 'OK'.

    Raises:
    TypeError: If the field_name is not a string.
    ValueError: If the field_name is not a column in the DataFrame.
    """
    if not isinstance(field_name, str):
        raise TypeError('Error: The field name is not a string.')
    if field_name not in df.columns:
        raise ValueError(f'Error: The field "{field_name}" is not found in the DataFrame.')

    if df[field_name].isnull().any():
        return 'KO'
    else:
        return 'OK'
