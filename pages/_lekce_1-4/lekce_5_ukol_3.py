import streamlit as st
import json

st.write("Úkol 3: ")
with open("menu.json", "r") as f:
    menu = json.load(f)

st.write(menu)

jidlo = st.text_input("Název jídla: ", key="jidlo")
cena = st.number_input("Cena jídla: ", key="cena", step=1)

if st.button("Přidej jídlo"):
    menu[jidlo] = cena
    with open("menu.json", "w") as f:
        json.dump(menu, f)
