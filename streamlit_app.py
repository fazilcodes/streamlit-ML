import streamlit as st
import pandas as pd

st.title('⚔️ Fazicodes/ML-streamlit')

st.info('Machine learning model')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
df
