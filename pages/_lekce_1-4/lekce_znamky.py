import streamlit as st
import json

try:
    with open("znamky.json", "r") as f:
        znamky = json.load(f)
except:
    znamky = {}

st.write(znamky)

jmeno = st.text_input("Jméno", key="jmeno")
znamka = st.number_input("Známka", step=1, min_value=1,
                         max_value=5, key="znamka")


if st.button("Přidej známku", key="confirm"):
    znamky[jmeno] = znamka
    with open("znamky.json", "w") as f:
        json.dump(znamky, f)
    st.write(znamky)
