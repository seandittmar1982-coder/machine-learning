import streamlit as st
import pandas as pd
st.title('Machine Learning App')

st.write('Hello world!')
df = pd.read_csv('penguins_cleaned.csv')
df
