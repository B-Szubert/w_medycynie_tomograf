import streamlit as st
st.write("""# My first app
 Hello *world!*""")

number=st.slider("Podaj liczbę skanów",90,720)
number=st.slider("Podaj liczbę dekoderów",90,720)
number=st.slider("Rozpiętość rozmieszczenia dekoderów jako % z długości przekątnej",25,100)
