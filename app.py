import streamlit as st
import requests
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
This is Anso's Website to predict the Taxi Fare of a ride within NY city - Have fun and enjoy
''')

pickup_datetime = st.sidebar.text_input("Date and Time", "2013-07-06 17:18:00 UTC")
pickup_longitude = st.sidebar.text_input("Pickup longitude", '-73.950655')
pickup_latitude = st.sidebar.text_input("Pickup latitude", "40.783282")
dropoff_longitude = st.sidebar.text_input("Dropoff longitude", "-73.984365")
dropoff_latitude = st.sidebar.text_input("Dropoff latitude", "40.769802")
passenger_count = st.sidebar.text_input("Passenger count", "1")

url = 'http://taxifare.lewagon.ai/predict_fare/'

#if url == 'http://taxifare.lewagon.ai/predict_fare/':

    #st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = dict(
    key=["2013-07-06 17:18:00.000000119"],
    pickup_datetime=[pickup_datetime],
    pickup_longitude=[float(pickup_longitude)],
    pickup_latitude=[float(pickup_latitude)],
    dropoff_longitude=[float(dropoff_longitude)],
    dropoff_latitude=[float(dropoff_latitude)],
    passenger_count=[int(passenger_count)])
response = requests.get(url, params=params)
prediction_fare = response.json()


st.markdown('''Prediction fare in $''')
st.markdown(round(prediction_fare['prediction'],2))
