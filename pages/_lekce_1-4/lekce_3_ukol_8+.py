import streamlit as st

st.write("Úkol 8:")
vek = st.number_input("Věk: ", step=1, key="vek1")
pohlavi = st.toggle("Muž", key="pohlavi")

if pohlavi:
    pohlavi_text = "muž"
else:
    pohlavi_text = "žena"

if vek >= 18:
    if pohlavi:
        vek_text = "jste plnoletý"
    else:
        vek_text = "jste plnoletá"
else:
    if pohlavi:
        vek_text = "nejste plnoletý"
    else:
        vek_text = "nejste plnoletá"

if st.button("Vypiš", key="confirm8"):
    st.write(f"Jste {pohlavi_text} a {vek_text}.")


st.write("Úkol 9:")
check1 = ""
check2 = ""
check3 = ""

if st.checkbox("Most", key="check9_1"):
    check1 = "Most"
if st.checkbox("Louny", key="check9_2"):
    check2 = "Louny"
if st.checkbox("Praha", key="check9_3"):
    check3 = "Praha"

mesta = " ".join([check1, check2, check3])
if st.button("Vybraná města", key="confirm9"):
    st.write(mesta)


st.write("Úkol 10:")
check1 = ""
check2 = ""
check3 = ""

if st.checkbox("Most", key="check10_1"):
    check1 = "Most"
if st.checkbox("Louny", key="check10_2"):
    check2 = "Louny"
if st.checkbox("Praha", key="check10_3"):
    check3 = "Prahu"
if st.toggle("s rodinou"):
    s_rodinou = "s rodinou"
else:
    s_rodinou = "bez rodiny"

vystup = ", ".join([check1, check2, check3, s_rodinou])
if st.button("Vypiš", key="confirm10"):
    st.write("Vybrali jste " + vystup)
