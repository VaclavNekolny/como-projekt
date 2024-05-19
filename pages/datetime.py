from datetime import datetime, timedelta
import streamlit as st


# st.write(datetime.now())        # když je letní čas, posun o 2h, jinak o 1h
# st.write(datetime.utcnow())     # universal time coordinates

# st.write(type(datetime.now()))    type = vrací typ funkce - co s ní mohu dělat...


# různé způsoby, jak zapsat datum
# "2024-12-31 23:59:59"
# "05/12/2024"
# "12.5.2024"

aktualni_cas = datetime.now()
st.write(aktualni_cas)

datum_1 = datetime.strptime("15.4.1993 15:30", "%d.%m.%Y %H:%M")
st.write(datum_1)

muj_vek = datetime.now() - datum_1
st.write(muj_vek)   # jak převedu počet dnů na roky, měsíce, dny....atp.
