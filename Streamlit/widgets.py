import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit text input")

name = st.text_input("Enter your name") 

if name:
    st.write(f"Hello, {name}!")

age = st.slider("Enter your age", min_value=0, max_value=120, step=1)
if age:
    st.write(f"You are {age} years old.")   


optios = st.multiselect("Select your favorite fruits", 
                         options=["Apple", "Banana", "Cherry", "Date"],
                         default=["Apple", "Cherry"])
if optios:
    st.write("You selected:", ", ".join(optios))   

options = st.selectbox("Select your country", 
                        options=["USA", "Canada", "India", "UK", "Australia"])
if options:
    st.write(f"You selected: {options}")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Here is the data from the uploaded file:")
    st.dataframe(df)    
    st.line_chart(df)
st.write("Here is a line chart of the dataframe:")

