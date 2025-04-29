
import streamlit as st

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="VERDIKTIA - IA de Internacionalización", layout="centered")

st.title("VERDIKTIA - Selección de Mercado Internacional para PYMEs")

# --- INPUTS ---
st.header("Datos de tu empresa")

producto = st.selectbox("Producto agroalimentario", ["Aceite de oliva", "Vino", "Fruta ecológica", "Conservas vegetales"])
comunidad = st.selectbox("Comunidad Autónoma", ["Andalucía", "La Rioja", "Murcia", "Valencia", "Castilla-La Mancha"])
certificaciones = st.multiselect("Certificaciones", ["BIO", "IFS", "BRC", "D.O."])
paises_actuales = st.multiselect("¿Dónde exportas actualmente?", ["Francia", "Italia", "Alemania", "Portugal", "México", "EE.UU."])
volumen = st.number_input("Volumen exportable mensual (en unidades/litros)", min_value=0)
canales = st.multiselect("Canales disponibles", ["Retail", "HORECA", "Online", "B2B"])
inversion = st.slider("Nivel de inversión disponible", 1, 5)
riesgo = st.slider("Nivel de riesgo aceptable", 1, 5)
preferencias_geo = st.multiselect("Preferencias geográficas", ["UE", "Latinoamérica", "MENA", "Asia"])
idiomas = st.multiselect("Idiomas en el equipo", ["Inglés", "Francés", "Alemán", "Italiano"])

# --- BOTÓN PARA PROCESAR ---
if st.button("Generar Recomendación de Mercado"):

    # --- BASE DE DATOS SIMPLIFICADA DE PAÍSES ---
    paises = [
        {"nombre": "Alemania", "crecimiento": 4, "saturacion": 2, "aranceles": 0, "logistica": 3, "cultural": "UE", "certificados": ["BIO", "IFS"], "idioma": "Alemán"},
        {"nombre": "Chile", "crecimiento": 5, "saturacion": 1, "aranceles": 0, "logistica": 2, "cultural": "Latinoamérica", "certificados": ["D.O.", "BIO"], "idioma": "Español"},
        {"nombre": "Emiratos Árabes", "crecimiento": 3, "saturacion": 2, "aranceles": 5, "logistica": 2, "cultural": "MENA", "certificados": ["BRC"], "idioma": "Inglés"}
    ]

    resultados = []

    # --- PROCESAR CADA PAÍS ---
    for pais in paises:
        score = 0

        # Crecimiento del mercado
        score += pais["crecimiento"] * 25

        # Menor saturación es mejor
        score += (5 - pais["saturacion"]) * 20

        # Barreras arancelarias
        score += (5 - pais["aranceles"]) * 20

        # Coste logístico (aproximado)
        score += pais["logistica"] * 15

        # Compatibilidad cultural
        if pais["cultural"] in preferencias_geo:
            score += 10

        # Certificaciones reconocidas
        if any(cert in pais["certificados"] for cert in certificaciones):
            score += 5

        # Idioma compartido
        if pais["idioma"] in idiomas:
            score += 5

        resultados.append((pais["nombre"], score))

    # --- ORDENAR RESULTADOS ---
    resultados = sorted(resultados, key=lambda x: x[1], reverse=True)

    # --- OUTPUT ---
    st.subheader("🌍 Países Recomendados:")
    for pais, puntuacion in resultados[:2]:
        st.write(f"**{pais}** — Puntuación: {puntuacion}/500")
        st.caption("Estrategia sugerida: Contactar distribuidor especializado + participación en feria sectorial")
        st.caption(f"Nivel de confianza: {int((puntuacion/500)*100)}%")
