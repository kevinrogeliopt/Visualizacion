import streamlit as st
import pandas as pd

def mostrar():
    st.title("Resumen estadístico")
    
    # Cargar datos
    df = pd.read_csv("../Datos/OECD.csv")
    
    # Selección de año
    años = sorted(df['AÑO'].unique(), reverse=True)
    año_seleccionado = st.radio("Seleccione el año", años, index=0)
    
    # Filtrar datos por año seleccionado
    df_filtrado = df[df['AÑO'] == año_seleccionado]
    
    # Checkbox para desagrupar por OECD
    desagrupar_oecd = st.checkbox("Desagrupar por pertenencia a la OECD")
    
    if desagrupar_oecd:
        # Resumen para países de la OECD
        df_oecd = df_filtrado[df_filtrado['OECD'] == 'SI']
        promedio_oecd = df_oecd['OBS_VALUE'].mean()
        st.metric("Promedio de esperanza de vida (OECD)", f"{promedio_oecd:.2f} años")
        
        # Resumen para países no OECD
        df_no_oecd = df_filtrado[df_filtrado['OECD'] == 'NO']
        promedio_no_oecd = df_no_oecd['OBS_VALUE'].mean()
        st.metric("Promedio de esperanza de vida (No OECD)", f"{promedio_no_oecd:.2f} años")
    else:
        # Resumen general
        promedio = df_filtrado['OBS_VALUE'].mean()
        st.metric("Promedio de esperanza de vida", f"{promedio:.2f} años")
    
    # Otras métricas
    st.write("Otras métricas:")
    st.write(f"Desviación estándar: {df_filtrado['OBS_VALUE'].std():.2f}")
    st.write(f"Mínimo: {df_filtrado['OBS_VALUE'].min():.2f}")
    st.write(f"Máximo: {df_filtrado['OBS_VALUE'].max():.2f}")