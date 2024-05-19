import json
import streamlit as st

if "logged" not in st.session_state:
    st.session_state["logged"] = False

with open("users.json", "r") as f:
    users = json.load(f)

if st.session_state["logged"] == True:
    st.write(f"Přihlášený uživatel: {st.session_state["jmeno"]}, email: {
             st.session_state["email"]}")
else:
    st.write("Nepřihlášený uživatel.")

st.write("Přihlášní uživatele:")


username = st.text_input("Uživatelské jméno: ", key="username",
                         placeholder="Uživatelské heslo")
password = st.text_input(
    "Heslo", key="pass", type="password", placeholder="Heslo")

if st.session_state["logged"] == False:
    if st.button("Přihlásit se.", key="login"):
        for i in range(0, len(users["uzivatele"])):
            if users["uzivatele"][i]["prihlasovaci_jmeno"] == username:
                if users["uzivatele"][i]["heslo"] == password:
                    st.write("Přihlášení proběhlo úspěšně.")
                    st.session_state["logged"] = True
                    st.session_state["jmeno"] = users["uzivatele"][i]["prihlasovaci_jmeno"]
                    st.session_state["email"] = users["uzivatele"][i]["email"]
                    break
        if st.session_state["logged"] == False:
            st.write("Špatné přihlašovací jméno nebo heslo.")

else:
    if st.button("Odhlásit se.", key="logout"):
        st.write("Odhlášení proběhlo úspěšně.")
        st.session_state["logged"] = False
        st.session_state["jmeno"] = ""
        st.session_state["email"] = ""

st.write(st.session_state)
