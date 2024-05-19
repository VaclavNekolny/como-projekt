from datetime import datetime
import streamlit as st


rok = datetime.now().year
mesic = datetime.now().month
den = datetime.now().day

st.write(f"dnes je {den}.{mesic}.{rok}")

st.write("Zadejte přesný den narození:")
uzivatel_den = st.number_input("Den:", step=1, min_value=1, max_value=31)
uzivatel_mesic = st.number_input("Měsíc:", step=1, min_value=1, max_value=12)
uzivatel_rok = st.number_input("Rok:", step=1, min_value=1900, max_value=2024)

if (uzivatel_mesic > mesic):
    rok = rok - 1
    mesic = mesic + 12


st.write(f"Váš aktuální věk je {
         rok - uzivatel_rok} let, {mesic - uzivatel_mesic} měsíců a {den - uzivatel_den}")


# timestamp - převod datumu na desetinné číslo. Jak to funguje??
# pak nejspíš mohu odčítat čísla v timestamp a zpátky konvertovat do formátu data... nevím. Zjistím, jak to funguje

# timedelta()  funkce pro
