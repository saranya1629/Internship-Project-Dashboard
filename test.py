import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Project Dashboard", layout="wide")
st.title("📊 Project Analytics Dashboard")

df = pd.DataFrame({
    'Project': ['Sales Analysis','HR Report','Marketing','Finance Dashboard'],
    'Department': ['Sales','HR','Marketing','Finance'],
    'Status': ['Completed','Completed','In Progress','Completed'],
    'Hours': [10,12,8,9]
})

st.sidebar.header("🔍 Filters")
selected_dept = st.sidebar.multiselect("Select Department", df['Department'].unique(), default=df['Department'].unique())
filtered_df = df[df['Department'].isin(selected_dept)]

col1, col2, col3 = st.columns(3)

with col1:
    fig1 = px.bar(filtered_df, x='Department', y='Hours', title='Chart 1: Bar')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(filtered_df, names='Status', title='Chart 2: Pie')
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    fig3 = px.line(filtered_df, x='Project', y='Hours', title='Chart 3: Line')
    st.plotly_chart(fig3, use_container_width=True)

st.dataframe(filtered_df)
