import streamlit as st

poledni_menu = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59,
    "kebab": 89,
    "pho": 79,
    "řízek": 119,
    "knedlo-vepřo-zelo": 139,
    "steak": 449
}

st.write("Úkol 1: ")
st.write(f"Cena sendviče je {poledni_menu['sendvič']}kč.")

st.write("Úkol 2: ")
st.write(f"Cena steaku je {poledni_menu.get('steak', 500)}kč.")

st.write("Úkol 3:")
poledni_menu["nudle"] = 99
st.write(poledni_menu)

st.write("Úkol 4:")
st.write(poledni_menu.keys())

st.write("Úkol 5:")
st.write(poledni_menu.values())

st.write("Úkol 6:")
st.write(poledni_menu.items())

st.write("Úkol 7:")
del poledni_menu["hamburger"]
st.write(poledni_menu)
