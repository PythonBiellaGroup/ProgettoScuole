import streamlit as st
import polars as pl

st.title("🎮 Analisi Tempi di Risposta")

uploaded_file = st.file_uploader("Carica il file CSV", type="csv")

if uploaded_file is not None:
    # Lettura CSV con Polars
    df = pl.read_csv(uploaded_file)

    # Conversione tempo in secondi (da millisecondi)
    df = df.with_columns((pl.col("tempo_risposta") / 1000).alias("tempo_risposta_sec"))

    st.subheader("📄 Prime 3 righe")
    st.dataframe(df.head(3))

    # Calcolo statistiche sulla colonna in secondi
    tempo_min = df["tempo_risposta_sec"].min()
    tempo_max = df["tempo_risposta_sec"].max()
    tempo_mean = df["tempo_risposta_sec"].mean()

    st.subheader("📊 Statistiche Tempo di Risposta (secondi)")

    col1, col2, col3 = st.columns(3)

    col1.metric("⚡ Risposta più veloce", f"{tempo_min:.2f} s")
    col2.metric("🐢 Risposta più lenta", f"{tempo_max:.2f} s")
    col3.metric("📈 Tempo medio", f"{tempo_mean:.2f} s")
