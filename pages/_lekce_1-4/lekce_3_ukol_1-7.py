import streamlit as st

cislo1 = st.number_input("Zadejte 1. číslo: ", step=1, key="cislo1")
cislo2 = st.number_input("Zadejte 2. číslo: ", step=1, key="cislo2")

check = st.checkbox("můžu?")

if st.button("Dělej") and bool(check):
    if cislo1 > cislo2:
        st.write(f"číslo {cislo1} je větší než číslo {cislo2}")
    elif cislo1 < cislo2:
        st.write(f"číslo {cislo1} je menší než číslo {cislo2}")
    else:
        st.write("čísla jsou stejná.")


st.write("Úkol 3:")

pocet_bodu = st.number_input(
    "Počet bodů: ", key="pocet_bodu", step=5, max_value=100)
if 100 >= pocet_bodu >= 91:
    st.write("Výborný.")
elif 91 > pocet_bodu >= 81:
    st.write("Chvalitebný.")
elif 81 > pocet_bodu >= 71:
    st.write("Dobrý.")
elif 71 > pocet_bodu >= 61:
    st.write("Dostatečný.")
else:
    st.write("Nedostatečný.")


st.write("Úkol 4:")

body = st.number_input(label="body", step=1,
                       max_value=100, key="pocet_bodu1")
oceneni = st.number_input(label="oceneni", step=1, key="pocet_oceneni")


# 1. varianta
# if st.button("Výsledek"):
#     if (body <= 60 and oceneni >= 20) or (61 <= body <= 70 and oceneni >= 5) or (71 <= body <= 80 and oceneni >= 2) or (81 <= body <= 90 and oceneni >= 5) or (71 <= body and oceneni >= 5):
#         st.write(f"Přijat. Počet bodů: {body}. Počet ocenění: {oceneni}.")
#     else:
#         st.write(f"Nepřijat. Počet bodů: {body}. Počet ocenění: {oceneni}.")


# Too many boolean expression - how can I fix it?


if st.button("Výsledek"):
    if body <= 60 and oceneni >= 20:
        st.write(f"Přijat. \n Počet bodů: {body}. \nPočet ocenění: {
                 oceneni}.")  # Jak udělat new line??
    elif 61 <= body <= 70 and oceneni >= 5:
        st.write(f"Přijat. Počet bodů: {body}. Počet ocenění: {oceneni}.")
    elif 71 <= body <= 80 and oceneni >= 2:
        st.write(f"Přijat. Počet bodů: {body}. Počet ocenění: {oceneni}.")
    elif 81 <= body <= 90 and oceneni >= 1:
        st.write(f"Přijat. Počet bodů: {body}. Počet ocenění: {oceneni}.")
    elif 71 <= body and oceneni >= 5:
        st.write(f"Přijat. Počet bodů: {body}. Počet ocenění: {oceneni}.")
    else:
        st.write(f"Nepřijat. Počet bodů: {body}. Počet ocenění: {oceneni}.")


st.write("Úkol 5:")
rok = st.number_input("rok", step=1, max_value=3000)

if st.button("Počítej") and rok > 0:
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        st.write("Je přestupný rok.")
    else:
        st.write("Není přestupný rok.")
else:
    st.write("Špatně zadaný rok.")


# Přidal bych tam trochu víc textu o tom, že gregoriánský kalendář upřesnil tuhle podmínku.
# Za pžestupný rok se nepovažují dny dělitené 100, pokud nejsou dělitelné zároveň 400.


st.write("Toggle, Checkbox:")
if st.toggle("Muž"):
    st.write("Jste muž")
else:
    st.write("Jste žena")

if st.checkbox("Muž"):
    st.write("Jste muž")
else:
    st.write("Jste žena")


st.write("Úkol 7:")
jmeno = st.text_input("Jméno: ", key="jmeno7")
prijmeni = st.text_input("Příjmení: ", key="prijmeni7")
muz = st.toggle("Muž", key="muz")

if (muz):
    pohlavi = "muž"
else:
    pohlavi = "žena"

if st.button("Představit se:"):
    st.write(f"Ahoj, já jsem {jmeno} {prijmeni} a jsem {pohlavi}.")
