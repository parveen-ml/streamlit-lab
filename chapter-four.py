import streamlit as st
import pandas as pd

st.title("Chai sales dashboard")

file = st.file_uploader("Upload your csv file", type= ["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file: 
    areas = df['Property_Area'].unique()
    selected_area = st.selectbox("Filter by Areas", areas)
    filtered_data = df[df["Property_Area"]==selected_area]
    st.dataframe(filtered_data)



