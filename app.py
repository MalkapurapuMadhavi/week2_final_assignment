import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📈 Smart Analytics Tool")


# CSV Upload
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Dataset Preview
    st.header("Dataset Preview")
    st.write(df.head())


    # Missing Values
    st.header("Missing Value Analysis")

    missing = df.isnull().sum()

    st.write(missing)


    # Statistics
    st.header("Basic Statistical Summary")

    st.write(df.describe())


    st.header("Dynamic Visualizations")


    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns


    if len(numeric_columns) >= 2:

        # Chart 1
        fig1 = px.scatter(
            df,
            x=numeric_columns[0],
            y=numeric_columns[1],
            title="Scatter Plot"
        )

        st.plotly_chart(fig1)


        # Chart 2
        fig2 = px.histogram(
            df,
            x=numeric_columns[0],
            title="Histogram"
        )

        st.plotly_chart(fig2)


        # Chart 3
        fig3 = px.box(
            df,
            y=numeric_columns[0],
            title="Box Plot"
        )

        st.plotly_chart(fig3)

    else:
        st.warning(
            "Need at least 2 numeric columns for charts"
        )


else:

    st.info("Please upload a CSV file to start analysis")