import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

data = load_data()
st.title('EDA - US Vehicles Dataset')

st.header('Odometer information')
hist_check = st.checkbox('Odometer Values of the Vehicles')
if hist_check:
    # Write a message:
    st.write('Histogram: Odometer values')
    # Graph the info
    fig = px.histogram(data, x="odometer", labels= {'odometer':'Odometer (km)'})
    #show graph
    st.plotly_chart(fig, use_container_width=True)


disp_check = st.checkbox('Price of vehicles according to Odometer')
if disp_check:
    # Write a message:
    st.write('Scatter plot: Price based on odometer values')
    # Graph the info
    fig = px.scatter(data, x="odometer", y="price", labels= {'odometer':'Odometer (km)', 'price':'Price (USD)'})
    #show graph
    st.plotly_chart(fig, use_container_width=True)

cond_check = st.checkbox('Condition of vehicles according to Odometer')
if cond_check:
    # Write a message:
    st.write('Histogram: Condition of vehicles based on odometer values')
    # Graph the info
    fig = px.histogram(data, x="odometer", labels= {'odometer':'Odometer (km)'}, color="condition")
    #show graph
    st.plotly_chart(fig, use_container_width=True)

st.header('Vehicles type by Manufacturer')
data['manufacturer'] = data['model'].str.split(' ').apply(lambda x: x[0])
fig = px.bar(data, x="manufacturer", color="type", labels= {'manufacturer':'Manufacturer'})
st.plotly_chart(fig, use_container_width=True)

st.header('Histogram of condition VS Model year')
fig2 = px.histogram(data, x="model_year", labels= {'model_year':'Model Year'}, color="condition")
st.plotly_chart(fig2, use_container_width=True)

st.header('Compare price distribution between manufacturers')
options = data['manufacturer'].unique()
st.write('Select manufacturer 1:')
manu_1 = st.selectbox('Select option...', options=options, key =1)
st.write('Select manufacturer 2:')
manu_2 = st.selectbox('Select option...', options=options, key =2)
data_filtered = data[(data['manufacturer']==manu_1) | (data['manufacturer']==manu_2)]

normalized_check = st.checkbox('Normalize histogram')
if normalized_check:
    fig3 = px.histogram(data_filtered, x="price", labels= {'model_year':'Model Year'}, color="manufacturer", histnorm='percent')
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.histogram(data_filtered, x="price", labels= {'model_year':'Model Year'}, color="manufacturer", histnorm='probability')
    st.plotly_chart(fig3, use_container_width=True)