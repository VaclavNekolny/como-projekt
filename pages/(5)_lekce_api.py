import streamlit as st
import json
import requests


api_key = "Q9SQDOS36Q12W6CD"

symbol_firmy = "FIAX"

data = requests.get(
    f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol_firmy}&apikey={api_key}")
data = data.json()

st.write(data)
