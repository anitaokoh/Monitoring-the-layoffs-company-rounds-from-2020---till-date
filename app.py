import streamlit as st
from src.visualizations_functions import line_chart, bar_charts, metric_chart, heat_map, choropleth_map
from src.metrics_computations import value_counts_metrics, other_single_metrics, update_date
from src.data_transformation import transform_raw_data, data_transformed_for_viz


# data source

data_file = 'layoffs_data.csv'


# Main Function

def home():
    """
    Main function to display the dashboard.
    """
    data = transform_raw_data(data_file, 'Date')
    percentage_coverage, year_2023, count_of_fire = other_single_metrics(data, 'year', '2023', '2022', 'Company')
    status_date = update_date()

    data_transformed_dict = {
        "data_for_bar_one": data_transformed_for_viz(data, 'Industry'),
        "data_for_bar_two": data_transformed_for_viz(data, 'year', 'Company'),
        "data_for_line": data_transformed_for_viz(data, 'Date'),
        "data_for_map_one": data_transformed_for_viz(data, 'Country')
    }

    # Section 1: Metrics
    c1, c2 = st.columns(2, gap='large')
    with c1:
        metric_chart("Total fire rounds in 2023", f"{year_2023:,.0f}",
                     f"{percentage_coverage}% of 2022 fire rounds as at {status_date}", arrow_direction="inverse")

    with c2:
        metric_chart("Company with the most fire rounds between 2020-2023", value_counts_metrics(data, 'Company'),
                     f"{count_of_fire} rounds as at {status_date}", arrow_direction="inverse")

    st.markdown("""---""")

    # Section 2: Tabs - Layoff Count Over time and Company Origin Count
    tab1, tab2 = st.tabs(["Layoff Count Over time", "Company Origin Count"])
    with tab1:
        st.markdown(""" ### Fire rounds Over time""")
        line_chart(data_transformed_dict["data_for_line"], 'Date', 'count')
        st.write(value_counts_metrics(data, "Date"), "is the date with the most fire so far and then the second highest date is",
                 value_counts_metrics(data, "Date", number=1), "and the third highest date is on",
                 value_counts_metrics(data, "Date", number=2))
    with tab2:
        st.markdown(""" ### Company Origin of Fire rounds """)
        choropleth_map(data_transformed_dict["data_for_map_one"], 'Country', 'count',
                       color_scale='Reds', locationmode='country names')
        st.write("Most of the companies who had fire rounds were in", value_counts_metrics(data, "Country"))

    st.markdown("""---""")

    # Section 3: Fire rounds by Industry Over time and Total Unique Company Fire rounds for each year
    c3, c4 = st.columns((7, 3))
    with c3:
        st.markdown(""" #### Fire rounds by Industry Over time""")
        bar_charts(data_transformed_dict["data_for_bar_one"], "Industry", "count")
        st.write(value_counts_metrics(data, "Industry"), "Industry was affected the most compared to other Industry and, \
                 ",  value_counts_metrics(data, "Industry", number=-1), "is the least.")
    with c4:
        st.markdown("""#### Total Unique Company Fire rounds for each year""")
        bar_charts(data_transformed_dict["data_for_bar_two"], "year", "Company", direction='horizontal', height=347)
        st.write("At at", status_date, "," ,value_counts_metrics(data, "year", 'Company'), \
                 "has the most unique company fire rounds. \n Note that", value_counts_metrics(data, "year"), \
                "also has the most fire rounds so far" )

    st.markdown("""---""")

    # Section 4: Heatmap Industry and Heatmap Stage
    tab3, tab4 = st.tabs(["Heatmap Industry", "Heatmap Stage"])
    with tab3:
        st.markdown("""### Heatmap of Industry Fire rounds over the months""")
        heat_map(data, 'FirstDayOfMonth', 'Industry')
    with tab4:
        st.markdown("""### Heatmap of  Fire rounds of Company in different Stages over the months""")
        heat_map(data, 'FirstDayOfMonth', 'Stage')


if __name__ == '__main__':
    st.set_page_config(page_title="Layoffs 2020-till date", page_icon="🧑‍🏭", layout='wide', initial_sidebar_state='expanded')
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.sidebar.header('About Dashboard')
    st.sidebar.write("""
    This Dashboard was created the monitor the layoffs data which was sourced from [here](https://www.kaggle.com/datasets/theakhilb/layoffs-data-2022).
    Dashboard repo can be found [here](https://github.com/your/repository).
    """)
                 
    st.sidebar.markdown('''
    ---
    Created with ❤️ by [Anita](https://www.linkedin.com/in/anita-okoh/).
    ''')    
    st.title("🔔  Layoffs Between 2020 - Till Date")
    home()
