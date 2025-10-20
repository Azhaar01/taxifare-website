import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

date = st.date_input('please enter date as (YYYY-MM-DD)', value= datetime.date(2012, 5, 2))
time = st.time_input('please enter time', value= datetime.time(7, 56, 0))
Datetime = f'{date} {time}'
pickup_longitude = st.number_input('please enter pickup longitude', value= -73.950655)
pickup_latitude = st.number_input('please enter pickup latitude', value= 40.783282)
dropoff_longitude = st.number_input('please enter dropoff longitude', value= -73.984365)
dropoff_latitude = st.number_input('please enter dropoff latitude', value= 40.783282)
passenger_count = st.number_input('please enter passenger count', value= 2)

url = 'https://taxifare-747325269837.europe-west1.run.app/predict'

if url == 'https://taxifare-747325269837.europe-west1.run.app/predict':
    params = {
        'pickup_datetime': Datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        predict= response.json()
        if st.button('Make Prediction'):
            st.header(f'Predicted fare: {round(predict["fare"], 2)}')
    else:
        st.error('Oh, There is an error. Try to catch it!')
