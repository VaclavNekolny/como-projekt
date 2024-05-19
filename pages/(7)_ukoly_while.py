import streamlit as st


cislo = st.number_input("Zadejte číslo: ", key="cislo", step=1)

i = 0
if st.button("Dělej"):
    while i <= cislo:
        st.write(i)
        i = i + 2


st.write("Úkol 6:")
