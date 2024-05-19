import json
import streamlit as st


try:
    with open("jidla.json", "r") as f:
        jidla = json.load(f)
except:
    jidla = {}

jidlo = st.text_input("Jídlo: ", key="food", placeholder="název jídla")
cena = st.number_input("Cena: ", key="price", step=1)


jidla[jidlo] = cena

if st.button("Přidej jídlo", key="confirm"):
    with open("jidla.json", "w") as f:
        json.dump(jidla, f)
    st.write(jidla)
