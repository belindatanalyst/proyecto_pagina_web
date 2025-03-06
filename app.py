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

# Nueva Gráfica
st.subheader("Histogram of condition vs model_year")

fig_hist = px.histogram(car_data, x="model_year", color="condition")

# Mostrar en Streamlit
st.plotly_chart(fig_hist)

# Nueva Gráfica: Distribución de precios por fabricante
st.subheader("Compare price distribution between manufacturers")

# Obtener una lista única de fabricantes para los selectores
manufacturers = car_data['manufacturer'].unique()

# Selección de dos fabricantes
manufacturer_1 = st.selectbox("Select manufacturer 1", manufacturers)
manufacturer_2 = st.selectbox("Select manufacturer 2", manufacturers)

# Casilla de verificación para normalizar el histograma
normalize_hist = st.checkbox("Normalize histogram", value=False)

# Filtrar el DataFrame para incluir solo los dos fabricantes seleccionados
df_filtered = car_data[car_data['manufacturer'].isin([manufacturer_1, manufacturer_2])]

# Crear el gráfico de cajas (box plot) para comparar la distribución de precios
fig_box = px.box(df_filtered, x="percent", y="price")

# Mostrar en Streamlit
st.plotly_chart(fig_box, use_container_width=True)
