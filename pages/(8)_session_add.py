import json
import streamlit as st

st.write("Přidání nového uživatele do databáze uživatelů.")

# úkol   přidej přes formulář :  Přihlašovací jméno,   heslo,  jméno,  emali

with open("users.json", "r") as f:
    users = json.load(f)

username = st.text_input("Přihlašovací jméno: ", key="username")
password = st.text_input("Heslo: ", key="password", type="password")
name = st.text_input("Jméno: ", key="name")
mail = st.text_input("E-mail: ", key="mail")


novy_uzivatel = {
    "prihlasovaci_jmeno": username,
    "heslo": password,
    "jmeno": name,
    "email": mail
}


if st.button("Ulož do databáze."):
    users["uzivatele"].append(novy_uzivatel)

st.write(users["uzivatele"])

with open("users.json", "w") as f:
    json.dump(users, f)
