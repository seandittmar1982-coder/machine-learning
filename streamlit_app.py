import streamlit as st
import pandas as pd
st.title('Machine Learning App')

df = pd.read_csv('penguins_cleaned.csv')
with st.expander('Data'):
  st.write('**Raw Data**')
  df

  st.write('**X**)
  x = df.drop('species', axis=1
  
