import streamlit as st
import pandas as pd

# Cargar datos
@st.cache
def cargar_datos():
    data_path = 'CargoFuncionCompetencia.xlsx'
    data = pd.read_excel(data_path)
    return data

data = cargar_datos()

# Título de la aplicación
st.title("Visualizador de Cargos y Funciones")

# Selector de dirección
direccion_seleccionada = st.selectbox("Selecciona una Dirección", data['idDireccion'].unique())

# Filtrar cargos por dirección seleccionada
cargos_filtrados = data[data['idDireccion'] == direccion_seleccionada]

# Selector de cargos
cargo_seleccionado = st.selectbox("Selecciona un Cargo", sorted(cargos_filtrados['Nombre'].unique()))

# Filtrar funciones y competencias por cargo seleccionado
resultados_finales = cargos_filtrados[cargos_filtrados['Nombre'] == cargo_seleccionado]

# Mostrar funciones
st.subheader("Funciones:")
for funcion in resultados_finales['funcion'].unique():
    st.text(funcion)

# Mostrar competencias
st.subheader("Competencias:")
for competencia in resultados_finales['competencia'].unique():
    st.text(competencia)


