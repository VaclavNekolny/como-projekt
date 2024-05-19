import json
import streamlit as st

if "logged" not in st.session_state:
    st.session_state["logged"] = False

with open("users.json", "r") as f:
    users = json.load(f)

if st.session_state["logged"] == True:
    st.write(f"Přihlášený uživatel: {st.session_state["jmeno"]}, email: {
             st.session_state["email"]}")
else:
    st.write("Nepřihlášený uživatel.")
