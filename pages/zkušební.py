import json
import pandas as pd
import streamlit as st

jidla = [
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
]

# CSV soubor na ukládání tabulek
# Pandas práce s tabulkama
# css pro nastavení pozadí v tabulce

st.dataframe(data=jidla, width=404, height=400)
