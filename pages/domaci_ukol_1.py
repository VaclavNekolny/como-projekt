import streamlit as st
import json


# načítá data ze souboru
try:
    with open("uzivatele.json", "r") as f:
        uzivatele = json.load(f)
except:
    uzivatele = {}


st.write(uzivatele)

jmeno = st.text_input("Jméno: ", key="name")
heslo = st.text_input("Heslo: ", key="pass", type="password", max_chars=15)
uzivatele[jmeno] = heslo

if st.button("Ulož data"):
    json.dump(uzivatele, open("uzivatele.json", "w"))
    st.write("Data uložena.")


with open("uzivatele.json", "r") as f:
    uzivatele = json.load(f)

uzivatel = st.selectbox("Uživatelské jméno: ", options=uzivatele,
                        key="user", placeholder="jméno zaměstnance")
heslo = st.text_input("Zadejte heslo: ", value="password",
                      key="heslo", type="password")

if st.button("Přihlásit"):
    if uzivatele[uzivatel] == heslo:
        st.write("Přihlášení úspěšné")
    else:
        st.write("Špatné uživatelské jméno nebo heslo")
