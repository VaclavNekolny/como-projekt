from datetime import datetime
import streamlit as st

datum_narozeni = st.number_input(
    "Rok narození: ", min_value=1910, max_value=2024, step=1, format="%i", key="rok_narozeni")
vek = datetime.now().year - datum_narozeni

st.write(f"Je vám {vek} let.")


st.write("Úkol 2:")
cislo1 = st.number_input("1. číslo: ", step=2, key="cislo_1")
cislo2 = st.number_input("2. číslo: ", step=1, key="cislo_2")

nejvetsi_cislo = max(cislo1, cislo2)
st.write(f"Největší číslo: {nejvetsi_cislo}")

rozdil_cisel = abs(cislo1 - cislo2)
st.write(f"Rozdíl čísel: {rozdil_cisel}")
