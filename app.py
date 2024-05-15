import streamlit as st
import pandas as pd

# Cargar los datos
@st.cache
def cargar_datos(filepath):
    data = pd.read_excel(filepath)
    return data

data = cargar_datos('CargoFuncionCompetencia.xlsx')

# Filtrar y ordenar los nombres de los cargos
cargos_unicos = data['Nombre'].drop_duplicates().sort_values()

# Selector de cargos en la interfaz
cargo_seleccionado = st.selectbox('Selecciona un cargo:', cargos_unicos)

# Mostrar funciones y competencias asociadas al cargo seleccionado
if cargo_seleccionado:
    st.write(f"Funciones y Competencias para el cargo: {cargo_seleccionado}")
    funciones = data[data['Nombre'] == cargo_seleccionado][['funcion', 'competencia']].drop_duplicates()
    for _, row in funciones.iterrows():
        st.subheader(f"Función: {row['funcion']}")
        competencias = data[(data['Nombre'] == cargo_seleccionado) & (data['funcion'] == row['funcion'])]['competencia']
        competencias = competencias.drop_duplicates().tolist()
        st.write("Competencias:")
        for competencia in competencias:
            st.write("- " + competencia)

