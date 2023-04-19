import streamlit as st
st.write("""# I'm just learning to write apps in Streamlit*""")

number_1=st.slider("Podaj liczbę skanów",90,720)
number_2=st.slider("Podaj liczbę dekoderów",90,720)
number_3=st.slider("Rozpiętość rozmieszczenia dekoderów jako % z długości przekątnej",25,100)

result=st.button("CLick!")
st.write(result)
