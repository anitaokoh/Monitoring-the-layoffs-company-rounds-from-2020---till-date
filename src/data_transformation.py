import pandas as pd


# Data Transformation

def transform_raw_data(data_file, column):
    """
    Read and transform the data from the given file.
    Args:
        data_file (str): Path to the data file.
        column (str): Name of the column containing the date.
    Returns:
        data (pd.DataFrame): Transformed data.
    """
    data = pd.read_csv(data_file, parse_dates=[column])
    data['year'] = data[column].dt.year
    data['year'] = data['year'].astype(str)
    data['FirstDayOfMonth'] = data[column] - pd.offsets.MonthBegin(1)
    return data

def data_transformed_for_viz(data, column_one, column_two=None):
    """
    Perform data transformation for the given columns.
    Args:
        data (pd.DataFrame): Data to perform transformation.
        column_one (str): Name of the first column.
        column_two (str, optional): Name of the second column. Defaults to None.
    Returns:
        data_transform (pd.DataFrame): Transformed data.
    """
    if column_two is not None:
        data_transform = data.groupby(column_one, as_index=False)[column_two].nunique()
    else:
        data_transform = data.groupby(column_one, as_index=False).size().rename(columns={'size':'count'})
    return data_transform