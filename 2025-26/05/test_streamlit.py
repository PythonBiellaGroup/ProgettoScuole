import streamlit as st
import polars as pl

# TITOLO PRINCIPALE
st.title("🎮 Test Streamlit")

# TESTO SEMPLICE
#st.write("Funziona! Questa è la mia prima app Streamlit.")

# CREIAMO ALCUNI DATI DI ESEMPIO
# df = pl.DataFrame({
#     "studente": ["Alice", "Bob", "Charlie"],
#     "punteggio": [18, 15, 20]
# })

# MOSTRIAMO LA TABELLA
# st.dataframe(df)

# CREIAMO UN GRAFICO
# st.bar_chart(df, x="studente", y="punteggio")