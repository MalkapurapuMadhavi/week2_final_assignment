import streamlit as st
import pandas as pd
import plotly.express as px


st.title("🏏 IPL Auction Analytics Dashboard")


df = pd.read_csv("ipl_auction.csv")


st.subheader("Dataset Preview")
st.write(df.head())


# Data Cleaning
df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)


# KPIs
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Players", len(df))
col2.metric("Teams", df["Team"].nunique())
col3.metric("Highest Price", df["Price"].max())


# Filter
st.sidebar.header("Filters")

team = st.sidebar.multiselect(
    "Select Team",
    df["Team"].unique()
)

if team:
    df = df[df["Team"].isin(team)]


# Visualization 1
fig1 = px.bar(
    df,
    x="Team",
    y="Price",
    title="Team Wise Spending"
)

st.plotly_chart(fig1)


# Visualization 2
fig2 = px.pie(
    df,
    names="Role",
    title="Player Role Distribution"
)

st.plotly_chart(fig2)


# Visualization 3
fig3 = px.bar(
    df.sort_values("Price", ascending=False).head(10),
    x="Player",
    y="Price",
    title="Top Expensive Players"
)

st.plotly_chart(fig3)


# Visualization 4
fig4 = px.histogram(
    df,
    x="Country",
    title="Players Country Distribution"
)

st.plotly_chart(fig4)


# Visualization 5
fig5 = px.scatter(
    df,
    x="Age",
    y="Price",
    title="Age vs Price"
)

st.plotly_chart(fig5)