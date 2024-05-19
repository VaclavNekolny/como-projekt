import datetime as dt
import streamlit as st
import pandas as pd

st.header("Pandas")

df_jmena = pd.read_csv("csv.csv", sep=",")
st.dataframe(df_jmena)

st.markdown("""Výběr sloupce z DataFrame""")

st.write(df_jmena["jmeno"])
# st.write(df_jmena[["jmeno", "prijmeni"]])
