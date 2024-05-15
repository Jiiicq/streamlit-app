import streamlit as st
import pandas as pd

# Cargar los datos
data = pd.read_excel('CargoFuncionCompetencia.xlsx')

# Filtrar las columnas y los registros activos
data = data[data['Activo'] == 1][['Nombre', 'funcion']].drop_duplicates()

# Ordenar los cargos de la A a la Z
data.sort_values('Nombre', inplace=True)

# Crear un selector en la barra lateral para elegir un cargo
selected_cargo = st.sidebar.selectbox('Seleccione un cargo:', data['Nombre'].unique())

# Mostrar las funciones asociadas al cargo seleccionado
st.write(f"Funciones para el cargo: {selected_cargo}")
functions = data[data['Nombre'] == selected_cargo]['funcion']
for function in functions:
    st.write("- ", function)
