import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import datetime

# Load File

with open('./src/model_best.pkl', 'rb') as file:
    best_pipe = pickle.load(file)

def run():
    # Title
    st.title('Equipment in Smart Manufacturing for Predictive Maintenance')

    # Sub Header
    st.subheader('Equipment Predictive Maintenance Prediction')

    # Image
    image = Image.open('./src/image2.jpg')
    st.image(image)

    # Create form
    with st.form(key='maintenance-prediction'):

        st.markdown('Data ID')
        date = st.date_input("Select a date")
        time = st.time_input("Select a time")
        timestamp = datetime.datetime.combine(date, time)
        machine_id = st.text_input('Machine ID', value='---machine id--')

        st.markdown('Equipment Operation Parameters')
        temperature = st.number_input('Temperature', min_value=0.00, max_value=200.00, value=0.00)
        vibration = st.number_input('Vibration', min_value=-20.00, max_value=200.00, value=0.00)
        humidity = st.number_input('Humidity', min_value=0.00, max_value=85.00, value=0.00)
        pressure = st.number_input('Pressure', min_value=0.00, max_value=6.00, value=0.00)
        energy_consumption = st.number_input('Energy Consumption', min_value=0.00, max_value=6.00, value=0.00)

        st.markdown('Equipment Status and Condition')
        machine_status = st.selectbox('Machine Status', (0, 1), index=0, help='0 = not running, 1 = running')
        anomaly_flag = st.selectbox('Anomaly Flag', (0, 1), index=0, help='0 = normal temperature & vibration, 1 = extreme temperature & vibration')
        predicted_remaining_life = st.number_input ('Remaining life Prediction', min_value=0, max_value=500, value=0)
        failure_type = st.selectbox('Failure Type', ('Normal', 'Vibration Issue', 'Overheating', 'Pressure Drop', 'Electrical Fault'), index=0)
        downtime_risk = st.number_input('Downtime Risk Score', min_value=0.00, max_value=1.00, value=0.00, help='range from 0-1')

        submitted = st.form_submit_button('Predict')

    # Data inference
    data_inf_input = {
        'timestamp': timestamp,
        'machine_id': machine_id,
        'temperature': temperature,
        'vibration': vibration,
        'humidity': humidity,
        'pressure': pressure,
        'energy_consumption': energy_consumption,
        'machine_status': machine_status,
        'anomaly_flag': anomaly_flag,
        'predicted_remaining_life': predicted_remaining_life,
        'failure_type': failure_type,
        'downtime_risk': downtime_risk,
    }

    # Data frame
    st.markdown('Data Summary:')
    data_inference = pd.DataFrame([data_inf_input])
    st.dataframe(data_inference)

    st.markdown('Result:')
    if submitted:
        # Prediction (0/1)
        pred = best_pipe.predict(data_inference)
        if pred == 1:
            st.write('### Equipment NEEDS Maintenance')
        else:
            st.write('### Equipment NO NEED Maintenance')

if __name__ == '__main__':
    run()