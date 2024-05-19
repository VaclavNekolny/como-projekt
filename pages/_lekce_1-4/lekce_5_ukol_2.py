import streamlit as st
import json

st.write("Úkol 2: ")
with open("menu.json", "r") as f:
    menu = json.load(f)

st.write(menu)
menu["kuřecí nudle"] = 99
with open("menu.json", "w") as f:
    json.dump(menu, f)
