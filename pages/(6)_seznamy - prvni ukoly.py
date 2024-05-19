import streamlit as st

jmena = ["Adéla", "Albert", "Míša", "Jára", "David", "Martin", "Oksana"]

st.write("První úkoly se seznamy:")
jmena.append("Tomáš")
jmena.sort()
jmena.remove("David")
jmena.append("Adéla")

jmena_set = set(jmena)


st.write(jmena)
st.write(jmena_set)
st.write(list(jmena_set))
st.write(len(jmena_set))


st.write("další úkol")

jmena = ["Adéla", "Albert", "Míša", "Jára", "David", "Martin", "Oksana"]
vybrane_jmeno = st.multiselect(
    "Vyber jméno", options=jmena, default=None, placeholder="vyber...")

st.write(vybrane_jmeno)
