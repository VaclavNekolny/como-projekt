import datetime as dt
import streamlit as st


minimali_datum = dt.datetime.strptime("1.1.1900", "%d.%m.%Y")
datum_narozeni = st.date_input(
    "Vložte datum narození: ", key="datum", min_value=minimali_datum)
ted = dt.datetime.now()

st.write(type(minimali_datum))
