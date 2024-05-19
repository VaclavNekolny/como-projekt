import streamlit as st

for n in range(3):
    st.write("Ahoj!!")

cislo = st.number_input("Zadej číslo: ", key="cislo", step=1)

for i in range(1, cislo + 1):
    st.write(i)

for jmeno in ["Tomáš", "Jan", "Petr", "Jana", "Eva"]:
    st.write(f"Ahoj {jmeno}.")


for jmeno in ["Tomáš", "Jan", "Petr", "Jana", "Eva"]:

    if jmeno.endswith("a"):
        st.write(f"Dobrý den paní {jmeno}.")
    else:
        st.write(f"Dobrý den pane {jmeno}.")

st.write("Úkol 7: ")

cislo1 = st.number_input("Číslo: ", step=1, key="cislo1")

if st.button("počítej", key="confirm1"):
    for i in range(cislo1):
        st.write(f"cislo: {i}.")
        if i == 7:
            st.write("break!")
            break


st.write("Úkol 8:")

seznam_jmen = ["Tomáš", "Jana", "Petr", "Iva", "David"]
for jmeno in seznam_jmen:
    if jmeno == "Petr":
        continue
    st.write(jmeno)

st.write("Úkol 9:")
jidla = {
    "hamburger": 55,
    "polevka": 40,
    "kuřecí vývar": 45
}
st.write(jidla)
for jidlo in jidla:
    jidla[jidlo] = jidla[jidlo] * 1.3
st.write(jidla)
