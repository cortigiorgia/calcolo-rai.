import streamlit as st

st.set_page_config(page_title="Calcolo RAI", layout="centered")

st.title("📐 Calcolo Rapporto Aeroilluminante")

st.write("Inserisci i dati della stanza:")

superficie_pavimento = st.number_input(
    "Superficie del pavimento (m²)",
    min_value=0.0,
    step=0.1
)

superficie_finestre = st.number_input(
    "Superficie finestrata apribile (m²)",
    min_value=0.0,
    step=0.1
)

if st.button("Calcola"):
    if superficie_pavimento > 0:
        rai = superficie_finestre / superficie_pavimento
        st.success(f"RAI = {rai:.3f}")

        if rai >= 0.125:
            st.markdown("✅ **Conforme alla normativa (≥ 1/8)**")
        else:
            st.markdown("❌ **Non conforme alla normativa (< 1/8)**")
    else:
        st.error("La superficie del pavimento deve essere maggiore di zero.")
