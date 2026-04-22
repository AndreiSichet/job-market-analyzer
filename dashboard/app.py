import streamlit as st
import pandas as pd
st.title("Job Market Intelligence Dashboard")
df = pd.read_csv("data/jobs.csv")
st.subheader("Raw Data")
st.dataframe(df)
st.subheader("Jobs per Role")
st.bar_chart(df["keyword"].value_counts())
st.subheader("Top Companies")
st.bar_chart(df["company"].value_counts().head(10))