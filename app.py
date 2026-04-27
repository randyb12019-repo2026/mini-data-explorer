"""
Mini Data Explorer
==================
App de Streamlit para explorar visualmente cualquier CSV.
"""

import pandas as pd
import streamlit as st


# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title='Mini Data Explorer',
    page_icon='🔍',
    layout='wide',
)

st.title('🔍 Mini Data Explorer')
st.markdown(
    'Sube un CSV y explóralo de forma interactiva. '
    'Si no subes nada, se usa el dataset de ejemplo.'
)


# 2. CARGA DE DATOS
st.sidebar.header('⚙️ Configuración')

archivo_subido = st.sidebar.file_uploader(
    'Sube tu CSV',
    type=['csv'],
)

if archivo_subido is not None:
    df = pd.read_csv(archivo_subido)
    st.sidebar.success('✅ Archivo cargado')
else:
    df = pd.read_csv('../mini-data-explorer/datos.csv')
    st.sidebar.info('ℹ️ Usando dataset de ejemplo')


# 3. MÉTRICAS
col1, col2, col3 = st.columns(3)
col1.metric('📏 Filas', df.shape[0])
col2.metric('📐 Columnas', df.shape[1])
col3.metric('❓ Valores nulos', df.isnull().sum().sum())


# 4. VISTA PREVIA
st.subheader('👀 Vista previa')
st.dataframe(df.head(10), use_container_width=True)


# 5. ESTADÍSTICAS
st.subheader('📊 Estadísticas descriptivas')
st.dataframe(df.describe(), use_container_width=True)


# 6. GRÁFICO INTERACTIVO
st.subheader('📈 Gráfico interactivo')

columnas_numericas = df.select_dtypes(include='number').columns.tolist()
columnas_categoricas = df.select_dtypes(include='object').columns.tolist()

tipo_grafico = st.radio(
    '¿Qué quieres ver?',
    ['Distribución de una variable numérica', 'Frecuencia de una variable categórica'],
    horizontal=True,
)

if tipo_grafico == 'Distribución de una variable numérica' and columnas_numericas:
    columna = st.selectbox('Elige una columna numérica', columnas_numericas)
    st.bar_chart(df[columna])
elif tipo_grafico == 'Frecuencia de una variable categórica' and columnas_categoricas:
    columna = st.selectbox('Elige una columna categórica', columnas_categoricas)
    st.bar_chart(df[columna].value_counts())
else:
    st.warning('No hay columnas de ese tipo en el dataset.')