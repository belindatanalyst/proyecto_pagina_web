import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Vehicle Analysis')
hist_button = st.button('Build Histogram') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creating a histogram for the car sales listing dataset')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Build a histogram')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Build a histogram for the odometer column')

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
st.subheader("Tipos de Vehículos por Fabricante")

# Crear el gráfico de barras apiladas
fig_bar = px.bar(car_data,x="model", color="type", title="Vehicle types by manufacturer", barmode="stack")
 
st.plotly_chart(fig_bar, use_container_width=True)
