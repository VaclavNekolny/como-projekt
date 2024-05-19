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

st.write("Úkol 16:")
jidlo = st.text_input("Jídlo: ", key="jidlo16")
cena = st.number_input("Cena: ", step=1, key="cena16")

if st.button("Přidej do menu"):
    restaurace["Panda"][jidlo] = cena
    st.write(restaurace)


st.write("Úkol 17: ")
st.write(restaurace)

lokal = st.text_input("Restaurace", key="restaurace17")
jidlo = st.text_input("Jídlo", key="jidlo17")

if st.button("Řekni cenu jídla", key="cena17"):
    st.write(f"Cena {jidlo} v restauraci {lokal} je: {
             restaurace[lokal][jidlo]} kč.")

st.write("Úkol 18: ")
st.write(restaurace)

lokal = st.text_input("Jméno restaurace: ", key="restaurace18")

if st.button("Vypiš menu", key="confirm18"):
    try:
        st.write(restaurace[lokal])
    except:
        st.write("Něco se pokazilo.")


st.write("Úkol 19: ")
lokal = st.text_input("Jméno restaurace: ", key="restaurace19")

if st.button("Vypiš menu", key="confirm19"):
    if lokal in restaurace:
        st.write(restaurace[lokal].keys())
    else:
        st.write("Restaurace není v seznamu.")

st.write("Úkol 20:")
jidlo = st.text_input("Název jídla: ", key="jidlo20")
cena = st.number_input("Cena: ", key="cena20", step=1)

if st.button("Přidej položku", key="confirm20"):
    if jidlo in restaurace["Bilbo"]:
        st.write("Toto jídlo už je v menu.")
    else:
        if cena > 0:
            restaurace["Bilbo"][jidlo] = cena
            st.write(restaurace["Bilbo"])
        else:
            st.write("Cena musí být větší než 0.")


st.write("Úkol 21: ")
restaurace["McDonalds"] = {}

jidlo = st.text_input("Název jídla: ", key="jidlo21")
cena = st.number_input("Cena: ", key="cena21", step=1)

if st.button("Přidej položku", key="confirm21"):
    if jidlo in restaurace["McDonalds"]:
        st.write("Toto jídlo už je v menu.")
    else:
        if cena > 20:
            restaurace["McDonalds"][jidlo] = cena
            st.write(restaurace)
        else:
            st.write("Cena musí být větší než 20.")
