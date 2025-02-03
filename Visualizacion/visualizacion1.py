import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def mostrar():
    st.title("Visualización I: Distribución de la esperanza de vida")
    
    # Cargar datos
    df = pd.read_csv("../Datos/OECD.csv")
    
    # Selección de año
    años = sorted(df['AÑO'].unique(), reverse=True)  # Ordenar en orden descendente
    año_seleccionado = st.radio("Seleccione el año", años, index=0)
    
    # Filtrar datos por año seleccionado
    df_filtrado = df[df['AÑO'] == año_seleccionado]
    
    # Selección de comparación
    comparacion = st.radio("Comparar por", ["Género", "Pertenencia a la OECD"])
    
    # Gráfica de caja y bigotes
    fig, ax = plt.subplots()
    if comparacion == "Género":
        sns.boxplot(data=df_filtrado, x='SEXO', y='OBS_VALUE', ax=ax)
    else:
        sns.boxplot(data=df_filtrado, x='OECD', y='OBS_VALUE', ax=ax)
    
    st.pyplot(fig)