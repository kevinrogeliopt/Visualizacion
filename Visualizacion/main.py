import streamlit as st
import introduccion
import resumen
import visualizacion1
import visualizacion2

# Configuración de la página
st.set_page_config(page_title="Análisis de Esperanza de Vida", layout="wide")

# Menú de navegación
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Ir a", ["Introducción", "Resumen estadístico", "Visualización I", "Visualización II"])

if opcion == "Introducción":
    introduccion.mostrar()
elif opcion == "Resumen estadístico":
    resumen.mostrar()
elif opcion == "Visualización I":
    visualizacion1.mostrar()
elif opcion == "Visualización II":
    visualizacion2.mostrar()