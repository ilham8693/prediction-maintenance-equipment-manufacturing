import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title='Smart Manufacturing for Predictive Maintenance',
    layout='wide',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('Pages', ('EDA', 'Prediction'))

if page == 'EDA':
    eda.run()

else:
    prediction.run()