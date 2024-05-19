import streamlit as st
import json
import requests


data = requests.get("https://www.frankfurter.app/currencies")
data = data.json()

currencies = data.keys()
currency_selected = st.selectbox("Choose a currency: ", options=currencies)

result = requests.get(
    f"https://www.frankfurter.app/latest?from={currency_selected}")
result = result.json()

if st.button("DO!"):
    st.write(result)
