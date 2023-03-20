import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import streamlit as st

st.title('Welcome to an app')
st.write("**Starting** the *build* of `penguin app` :penguin: :mag:")
st.write("Data is taken from [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)")

st.header('Data')

data = pd.read_csv('penguins_extra.csv')

#st.write('Display a smale of 20 datapoints', df.sample(20))

species = st.selectbox(f"Select species", data.species.unique())

st.write(f"Displaying a sub data from {species}", data[data['species']==species])

fig, ax = plt.subplots()
ax = sns.scatterplot(
    data = data,
    x = 'bill_length_mm',
    y = 'flipper_length_mm',
    hue = 'species'
)
st.pyplot(fig)

st.bar_chart(data.groupby('island')['species'].count())

st.map(data)

slider_choice = st.sidebar.selectbox("You have the following options:", ['Yes','No'])

if slider_choice == 'Yes':
    st.write('yes selected')
else:
    st.write('no selected')

data_2 = st.sidebar.file_uploader('Upload data', type=['csv'])

if data_2 is not None:
    df1 = pd.read_csv(data_2)
    st.write(df1)


st.markdown(f"""
<style>
.stApp{{
    background-image: url(https://images.unsplash.com/photo-1551986782-d0169b3f8fa7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cGVuZ3VpbnN8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60);
    background-size: cover;
}}
</style>
""",unsafe_allow_html=True)
