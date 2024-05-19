from microfs import ls, rm, put, get, get_serial
import streamlit as st
import json

st.write(get_serial())

st.write(ls())

get("vystup.txt")

with open('vystup.txt') as my_file:
    vystup = my_file.read()
st.write(f"vystup.txt: {vystup}")
