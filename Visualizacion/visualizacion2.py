import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def mostrar():
    st.title("Visualización II: Evolución de la esperanza de vida")
    
    # Cargar datos
    df = pd.read_csv("../Datos/OECD.csv")
    
    # Selección de países
    paises = df['PAIS'].unique()
    paises_seleccionados = st.multiselect("Seleccione los países", paises, default=paises[:3])
    
    # Selección de género
    genero = st.radio("Seleccione el género", ['Total', 'Female', 'Male'])
    
    # Selección de rango de años
    años = sorted(df['AÑO'].unique(), reverse=True)  # Años en orden descendente
    año_inicial = st.selectbox("Seleccione el año inicial", años, index=len(años)-1)  # Por defecto, el más antiguo
    año_final = st.selectbox("Seleccione el año final", años, index=0)  # Por defecto, el más reciente
    
    # Validar que el año inicial sea menor o igual al año final
    if año_inicial > año_final:
        st.error("El año inicial debe ser menor o igual al año final.")
        return
    
    # Filtrar datos por países, género y rango de años
    df_filtrado = df[
        (df['PAIS'].isin(paises_seleccionados)) & 
        (df['SEXO'] == genero) & 
        (df['AÑO'] >= año_inicial) & 
        (df['AÑO'] <= año_final)
    ]
    
    # Ordenar los datos por año
    df_filtrado = df_filtrado.sort_values(by='AÑO')
    
    # Gráfica de líneas
    fig, ax = plt.subplots()
    for pais in paises_seleccionados:
        df_pais = df_filtrado[df_filtrado['PAIS'] == pais]
        ax.plot(df_pais['AÑO'], df_pais['OBS_VALUE'], label=pais)
    
    ax.set_xlabel("Año")
    ax.set_ylabel("Esperanza de Vida")
    ax.legend(title="País")
    ax.grid(True) #Cuadrícula
    
    st.pyplot(fig)