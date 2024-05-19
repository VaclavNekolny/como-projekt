import json
import streamlit as st


with open("menu6.json", "r", encoding="utf-8") as file:
    menu = json.load(file)

st.write(menu)
jidla = menu["jídla"]
napoje = menu["nápoje"]

jidlo = st.selectbox("Vyberte jídlo: ", jidla)
napoj = st.selectbox("Vyberte nápoj: ", napoje)
platba = st.selectbox("Platba: ", menu["platba"])

cena_jidla = jidla[jidlo]
cena_napoje = napoje[napoj]
celkova_cena = cena_jidla + cena_napoje

if st.button("spočítej cenu"):
    if platba == "kupón":
        st.write(f"Cena před slevou: {celkova_cena} kč.")
        st.write(f"Cena   po  slevě: {celkova_cena*0.9} kč.")
    else:
        st.write(f"Celková cena za menu je: {celkova_cena} kč.")

    st.write(f"---platba: {platba} ---")
