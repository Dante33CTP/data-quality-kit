def check_type(df, column_name, data_type) -> str:
    """
    Check if all non-null entries in a specified column of a DataFrame are of the specified data type.

    Args:
        df (pandas.DataFrame): The DataFrame to check.
        column_name (str): The name of the column to check.
        data_type (type): The expected data type of the column entries.

    Returns:
        str: 'OK: All records are of the specified type' if all non-null entries are of the specified data type.

    Raises:
        ValueError: If the column does not exist in the DataFrame or if at least one entry is not of the specified data type.
    """
    if column_name not in df.columns:
        raise ValueError(f'Error: The column {column_name} is not in the DataFrame')
    filtered_values = df[df[column_name].notnull()]
    if filtered_values[column_name].apply(lambda x: isinstance(x, data_type)).all():
        return 'OK: All records are of the specified type'
    else:
        raise ValueError('KO: At least one record is not of the specified type')
