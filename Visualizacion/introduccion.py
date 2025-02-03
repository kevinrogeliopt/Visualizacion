import streamlit as st

def mostrar():
    st.title("Introducción")
    st.write("""
    ### Autor: Kevin Peña
             
    Este conjunto de datos contiene información sobre la esperanza de vida en diferentes países, con un
    registro desde el 2015 hasta el 2023, desglosada por género y año. Los datos provienen de la
    organización OECD Data Explorer, y el objetivo principal es analizar cómo ha evolucionado la esperanza
    de vida a lo largo del tiempo, comparando diferentes géneros y la pertenencia a la OECD.

    ### Características del conjunto de datos:
    - **Origen de los datos**: OECD Data Explorer
    - **Indicadores**: Esperanza de vida (OBS_VALUE), Género (SEXO), Año (AÑO), Pertenencia a la OECD (OECD).
    - **Países**: 49 países, 38 pertenecen a la OECD y 11 no.
    - **Géneros**: Los datos se agrupan en 'Female', 'Male', y 'Total'.
    """)