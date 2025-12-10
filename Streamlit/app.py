import streamlit as st
import pandas as pd
import numpy as np

# title of the application
st.title("My First Streamlit App")

# display a simple text
st.write("Hello, welcome to my app!")

# display a dataframe
data = pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10)
})
st.write("Here is a random dataframe:")
st.dataframe(data)  

# create a simple line chart
st.line_chart(data)
st.write("Here is a line chart of the dataframe:") 