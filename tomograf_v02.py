import streamlit as st
st.write("""# I'm just learning to write apps in *Streamlit*""")
st.write(':otter:')

number_1=st.slider("Podaj liczbę skanów",90,720)
number_2=st.slider("Podaj liczbę dekoderów",90,720)
number_3=st.slider("Rozpiętość rozmieszczenia dekoderów jako % z długości przekątnej",25,100)

format_in = st.radio(
    "Plik jakiego formatu chcesz wczytać?",
    ('DICOM', 'bit_mapa'))
format_out = st.radio(
    "Plik jakiego formatu chcesz uzyskać?",
    ('DICOM', 'bit_mapa'))
usrednianie = st.radio(
    "Jaki sposób uśredniania preferujesz?",
    ('Brak uśrednienia', 'Najbliższe 4 punkty', 'propozycja pana B...'))
genre = st.radio(
    "Czy resultat ma się pokazywać przez cały czas, czy dopiero na końcu?",
    ('w trakcie obliczeń', 'dopiero na zakończenie'))


result=st.button("Rozpocznij ciężkie obliczenia!")
if(result):
    st.write(result)
