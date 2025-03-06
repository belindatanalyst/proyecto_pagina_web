import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Título de la sección de visualización de datos
st.title("Data Viewer")

# Inicializar el DataFrame para asegurarse de que existe
df = car_data.copy()

# Checkbox para filtrar modelos con menos de 1000 anuncios
include_small_mfr = st.checkbox("Include manufacturers with less than 1000 ads", value=True)

if not include_small_mfr:
    manufacturer_counts = car_data['model'].value_counts()
    df = car_data[car_data['model'].isin(manufacturer_counts[manufacturer_counts >= 1000].index)]

# Mostrar la tabla en Streamlit
st.dataframe(df)

# **Nueva Gráfica: Tipos de vehículos por fabricante**
st.subheader("Vehicle types by manufacturer")

car_data["manufacturer"] = car_data["model"].apply(lambda x: x.split()[0] if isinstance(x, str) else x)

# Crear el gráfico de barras apiladas
fig_bar = px.bar(car_data,x="manufacturer", color="type", barmode="stack")
 
st.plotly_chart(fig_bar, use_container_width=True)