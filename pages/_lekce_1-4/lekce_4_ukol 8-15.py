import streamlit as st

st.write("Úkol 8:")

restaurace = {
    "Bilbo": {
        "Řízek": 100,
        "Vepřový guláš": 120
    },
    "Lagarto": {
        "Avokádový toast": 130,
        "Tacos": 150
    },
    "Panda": {
        "Sushi": 200,
        "Ramen": 180
    }
}
st.write(restaurace)


st.write("Úkol 9:")
cena = restaurace["Lagarto"]["Avokádový toast"]
st.write(cena)

st.write("Úkol 10:")
restaurace["Bilbo"]["Řízek s bramborem"] = 150
st.write(restaurace)

st.write("Úkol 11:")
last = restaurace["Panda"].pop("Sushi")
st.write(restaurace)

st.write("Úkol 12:")
st.write(restaurace.keys())

st.write("Úkol 13:")
st.write(restaurace["Lagarto"].keys())

st.write("Úkol 14:")
st.write(restaurace["Bilbo"].values())

st.write("Úkol 15:")
st.write(restaurace["Panda"].items())
