import streamlit as st
import pandas as pd
import plotly.express as px
import plost



# Visualization Functions

def bar_charts(transformed_data, bar_name, value_name, color_code="#dc143c", direction=None, height=None):
    """
    Display a bar chart.
    Args:
        transformed_data (pd.DataFrame): Transformed data for the chart.
        bar_name (str): Name of the column for the bars.
        value_name (str): Name of the column for the values.
        color_code (str, optional): Color code for the bars. Defaults to "#dc143c".
        direction (str, optional): Direction of the bars. Defaults to None.
        height (int, optional): Height of the chart. Defaults to None.
    """
    return plost.bar_chart(
        data=transformed_data,
        bar=bar_name,
        value=value_name,
        color=color_code,
        direction=direction,
        use_container_width=True,
        height=height
    )

def heat_map(data, column_x, column_y, aggregate_metrics='count', height_size=600):
    """
    Display a heatmap.
    Args:
        data (pd.DataFrame): Data for the heatmap.
        column_x (str): Name of the column for the x-axis.
        column_y (str): Name of the column for the y-axis.
        aggregate_metrics (str, optional): Aggregation metrics for the heatmap. Defaults to 'count'.
        height_size (int, optional): Height of the chart. Defaults to 600.
    """
    return plost.xy_hist(
        data=data,
        x=column_x,
        y=column_y,
        aggregate=aggregate_metrics,
        use_container_width=True,
        height=height_size,
        x_bin=None,
        y_bin=None
    )

def metric_chart(metrics_title, value_to_display, delta_change, arrow_direction="inverse"):
    """
    Display a metric chart.
    Args:
        metrics_title (str): Title of the metric.
        value_to_display: Value to display.
        delta_change: Delta change value.
        arrow_direction (str, optional): Direction of the delta change arrow. Defaults to "inverse".
    """
    return st.metric(label=metrics_title, value=value_to_display, delta=delta_change, delta_color=arrow_direction)

def line_chart(data_transformed, column_x, column_y):
    """
    Display a line chart.
    Args:
        data_transformed (pd.DataFrame): Transformed data for the chart.
        column_x (str): Name of the column for the x-axis.
        column_y (str): Name of the column for the y-axis.
    """
    return st.line_chart(data_transformed, x=column_x, y=column_y)

def choropleth_map(data_transformed, column_x, color_value,  color_scale='Reds', locationmode='country names'):
    """
    Display a choropleth map.
    Args:
        data_transformed (pd.DataFrame): Transformed data for the map.
        column_x (str): Name of the column for the x-axis.
        color_value (str): Name of the column for the color value.
        title (str): Title of the map.
        color_scale (str, optional): Color scale for the map. Defaults to 'Reds'.
        locationmode (str, optional): Location mode for the map. Defaults to 'country names'.
    """
    fig = px.choropleth(data_frame=data_transformed, locations=column_x, locationmode=locationmode,
                        color=color_value, color_continuous_scale=color_scale)
    return st.plotly_chart(fig, theme="streamlit", use_container_width=True)