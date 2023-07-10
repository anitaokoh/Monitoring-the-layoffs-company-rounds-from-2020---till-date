from datetime import datetime, timedelta
import pandas as pd

# Metric Computation

def update_date():
    """
    Update the date to the first day of the current week (Monday).
    Returns:
        status_date (datetime.date): First day of the current week.
    """
    today = datetime.today().date()
    return today - timedelta(days=today.weekday())

def last_date(data, column_name):
    return data[column_name].max()


def value_counts_metrics(data, column_one, column_two=None, number=0):
    """
    Compute value counts metrics from the data.
    Args:
        data (pd.DataFrame): Data to compute metrics from.
        column_one (str): Name of the first column.
        column_two (str, optional): Name of the second column. Defaults to None.
        number (int, optional): Index of the value to return. Defaults to 0.
    Returns:
        result: Value counts metric.
    """
    if column_two is not None:
        result = data.groupby(column_one)[column_two].nunique().nlargest(1).index[number]
    else:
        result = data[column_one].value_counts().index[number]
    return result

def other_single_metrics(data, column_one, value_1, value_2, column_two):
    """
    Compute other single metrics based on data.
    Args:
        data (pd.DataFrame): Data to compute metrics from.
        column_one (str): Name of the first column.
        value_1: Value to compare in column_one.
        value_2: Value to compare in column_one.
        column_two (str): Name of the second column.
    Returns:
        percentage_coverage (float): Percentage coverage.
        count_1 (int): Count of value_1.
        count_of_fire (int): Count of column_two.
    """
    count_1 = data[data[column_one] == value_1].count().values[0]
    count_2 = data[data[column_one] == value_2].count().values[0]
    count_of_fire = data[column_two].value_counts().values[0]
    return round((count_1 / count_2) * 100, 2), count_1, count_of_fire