import streamlit as st
import pandas as pd

st.title('⚔️ Fazicodes/ML-streamlit')

st.info('Machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  df

  st.write('**X**')
  x = df.drop('species', axis=1)
  x
  
  st.write('**Y**')
  y = df.species
  y

with st.expander('Data Visualization'):
  # "bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex""bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g", color="species")

# preparations
with st.sidebar:
  st.header('Input Features')
  # "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island = st.selectbox('island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill Length in mm', 32.1, 59.6, 42.9)
  bill_depth_mm = st.slider('Bill Depth in mm', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper Length in mm', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body Mass in g', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('gender', ('male', 'female'))
  
# create df for input
data = {
  'island': island,
  'bill_length_mm': bill_length_mm,
  'bill_depth_mm': bill_depth_mm,
  'flipper_length_mm': flipper_length_mm,
  'body_mass_g': body_mass_g,
  'gender': gender,
} 

input_df = pd.DataFrame(data, index=[0])
input_df
