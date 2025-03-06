import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')


# Primer grafica
st.title("Data Viewer")
df = car_data.copy()
# Checkbox para filtrar modelos con menos de 1000 anuncios
include_small_mfr = st.checkbox("Include manufacturers with less than 1000 ads", value=True)

if not include_small_mfr:
    manufacturer_counts = car_data['model'].value_counts()
    df = car_data[car_data['model'].isin(manufacturer_counts[manufacturer_counts >= 1000].index)]

st.dataframe(df)


# Segunda grafica
st.subheader("Vehicle types by manufacturer")
car_data["manufacturer"] = car_data["model"].apply(lambda x: x.split()[0] if isinstance(x, str) else x)
# Crear la grafica de barras
fig_bar = px.bar(car_data,x="manufacturer", color="type", barmode="stack")
 
st.plotly_chart(fig_bar, use_container_width=True)


# Tercera grafica
st.subheader("Histogram of condition vs model_year")
fig_hist = px.histogram(car_data, x="model_year", color="condition")

st.plotly_chart(fig_hist)


# Cuarta grafica
st.subheader("Compare price distribution between manufacturers")
# Obtener una lista única de fabricantes para los selectores
manufacturers = car_data['model'].unique()
# Seleccion de dos fabricantes
manufacturer_1 = st.selectbox("Select manufacturer 1", manufacturers)
manufacturer_2 = st.selectbox("Select manufacturer 2", manufacturers)
# Casilla de verificacion 
normalize_hist = st.checkbox("Normalize histogram", value=False)
# Filtrar el dataFrame para incluir solo los dos fabricantes seleccionados
df_filtered = car_data[car_data['model'].isin([manufacturer_1, manufacturer_2])]
# Si la casilla esta marcada, normalizar el histograma
if normalize_hist:
    # Crear el grafico de histograma normalizado para comparar 
    fig_hist = px.histogram(df_filtered, x="price", color="m", histnorm="probability density")
else:
    # Crear el grafico de histograma sin normalizar para comparar 
    fig_hist = px.histogram(df_filtered, x="price", color="manufacturer")

st.plotly_chart(fig_hist, use_container_width=True)
