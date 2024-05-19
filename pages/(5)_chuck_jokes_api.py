import streamlit as st
import json
import requests


# response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
# data = response.json()

# klice = data["types"]
# st.write(klice)

# foto = data["sprites"]["front_default"]
# st.image(foto)       # foto nefunguje - nevím proč :/

categories = requests.get("https://api.chucknorris.io/jokes/categories")
categories = categories.json()
selected_category = st.selectbox("Choose a category:", options=categories)

if st.button("Tell me a joke."):
    data = requests.get(
        f"https://api.chucknorris.io/jokes/random?category={selected_category}")
    chuck_joke = data.json()
    st.write(chuck_joke["value"])
