import streamlit as st


st.write("Úkol 1:")
ukol_1 = st.text_input("Zadejte jméno: ", value="Jméno",
                       max_chars=5, key="jmeno_1")
st.write(ukol_1)


st.write("Úkol 2:")
ukol_2 = st.text_input("Zadejte přjmení: ", value="Příjmení",
                       key="prijmeni_1", label_visibility="hidden")
st.write(ukol_2)


st.write("Úkol 3:")
ukol_3 = st.text_input("Zadejte město: ", value="Město",
                       type="password", help="Zadejte město", key="mesto_1")
st.write(ukol_3)


st.write("Úkol 4:")
spojeni_pomoci_plus = ukol_1 + ukol_2 + ukol_3
st.write(spojeni_pomoci_plus)


st.write("Úkol 5:")
spojeni_pomoci_fstring = f"{ukol_1} {ukol_2} {ukol_3}"
st.write(spojeni_pomoci_fstring)
st.write(spojeni_pomoci_fstring.lower())
st.write(spojeni_pomoci_fstring.upper())
st.write(spojeni_pomoci_fstring.capitalize())

delka_textu = len(spojeni_pomoci_fstring)
st.write(f"délka textu: {delka_textu} znaků")


text = "Magistrát města Mostu  "
st.write(text.replace("Mostu", "Litvínova"))
st.write(text.startswith("Magi"))
st.write(text.endswith("m"))

text = "Magistrát města Mostu  "
st.write(f"délka textu: {len(text)} znaků")

ocisteny_text = text.strip()

st.write(f"délka očištěného textu: {len(ocisteny_text)} znaků")

pozice_slova = text.find("Mostu")
st.write(f"Pozice slova 'Mostu' je {pozice_slova}")


libovolny_retezec1 = "Magistrát"
libovolny_retezec2 = "města"
libovolny_retezec3 = "Mostu"
retezec_spojeny_mezerou = " _ ".join(
    [libovolny_retezec1, libovolny_retezec2, libovolny_retezec3])
retezec_spojeny_polmckou = "---".join([libovolny_retezec1,
                                       libovolny_retezec2, libovolny_retezec3])

st.write(retezec_spojeny_mezerou)
st.write(retezec_spojeny_polmckou)


st.write("Úkol 6:")
jmeno = st.text_input("Zadejte jméno: ")
prijmeni = st.text_input("Zadejte příjmení: ")

st.write(f"{jmeno.capitalize()} {prijmeni.capitalize()}")
