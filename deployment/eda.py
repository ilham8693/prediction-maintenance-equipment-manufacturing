import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # Title
    st.title('Equipment in Smart Manufacturing for Predictive Maintenance')

    # Sub Header
    st.subheader('Exploratory Data Analysis (EDA) of dataset')

    # Image
    image = Image.open('./src/image1.jpg')
    st.image(image, caption= "Factory Landscape")

    # DataFrame
    st.write('##### Data frame')
    df = pd.read_csv('./src/smart_manufacturing_dataset.csv')
    st.dataframe(df)

    # EDA distribution numerical
    st.write('##### Distribution plot numerical')
    fig = plt. figure(figsize=(15, 5))
    option = st.selectbox('Columns : ', ('temperature', 'vibration', 'humidity', 'pressure', 'energy_consumption', 'predicted_remaining_life', 'downtime_risk', 'maintenance_required'))
    sns.histplot(df[option], bins=30, kde=True)
    st.pyplot(fig)

      # EDA Heatmap correlation numerical with maintenance_required
    st.write('##### Heatmap correlation with maintenance_required')
    fig = plt. figure(figsize=(15, 10))
    sns.heatmap(df[['temperature', 'vibration', 'humidity', 'pressure', 'energy_consumption', 'predicted_remaining_life', 'downtime_risk', 'maintenance_required']].corr(), annot=True, cmap='coolwarm')
    st.pyplot(fig)

    # EDA distribution categorical vs maintenance_required
    st.write('##### Distribution plot categorical vs maintenance_required')
    fig = plt. figure(figsize=(15, 5))
    option = st.selectbox('Columns : ', ('machine_id', 'machine_status', 'anomaly_flag', 'failure_type'))
    sns.countplot(x=option, hue='maintenance_required', data=df)
    st.pyplot(fig)

    # EDA equipment that have maintenance_required=1
    top_machines = (
    df[df['maintenance_required'] == 1]
    .groupby('machine_id')
    .size()
    .sort_values(ascending=False))

    st.write('##### Equipment maintenance signal accumulation')
    fig = plt.figure(figsize=(15,5))
    sns.barplot(
    x=top_machines.index.astype(str),
    y=top_machines.values,
    hue=top_machines.index.astype(str),
    palette='rocket')
    st.pyplot(fig)

if __name__ == '__main__':
    run()