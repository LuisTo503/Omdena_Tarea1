
import streamlit as st
import pandas as pd
import cv2
import time
from streamlit_embedcode import github_gist
from streamlit.elements.image import Channels

st.title("1. Web Scraping")

# --- Titulo  descripcion del modulo  ---

st.subheader("Muestra del resultado del Web SCRAPING")


st.caption("Automatizamos el proceso de obtención de datos mediante el acceso y análisis del contenido HTML de la página web: https://ultimahora.sv/")
st.caption("")
st.divider()

# Cargar el DataFrame desde el archivo CSV
url_csv = "data\\Noticias_Ultima_Hora.csv"
data = pd.read_csv(url_csv)

# Ajustar el ancho y largo del DataFrame en el sidebar
ancho = st.sidebar.slider("Ajustar Ancho del DataFrame", 100, 800, 500)
largo = st.sidebar.slider("Ajustar Largo del DataFrame", 100, 800, 500)
tamanio_fuente = st.sidebar.slider("Tamaño de la Fuente", 10, 15, 10)

# Widget para seleccionar la columna de filtrado
columna_filtrado = st.selectbox("Seleccionar Columna para Filtrar", data.columns)

# Widget para ingresar el valor de filtrado
valor_filtrado = st.text_input(f"Ingresar valor para filtrar en la columna '{columna_filtrado}'")

# Filtrar el DataFrame
data_filtrado = data[data[columna_filtrado].str.contains(valor_filtrado, case=False, na=False)]

# Establecer el ancho máximo de la tabla con HTML y CSS
estilo_html = f"""
<style>
    .dataframe {{
        width: {ancho}px !important;
        max-height: {largo}px;
        overflow: auto;
        font-size: {tamanio_fuente}px;
    }}
</style>
"""
st.markdown(estilo_html, unsafe_allow_html=True)

# Mostrar DataFrame
st.dataframe(data_filtrado)


# --- DIVISION --    
st.divider() 

st.subheader("Mostrando el cuerpo de la noticia....")

# --- Mostraremos el contenido del archivo .TXT ---

def mostrar_contenido_txt():
    # Archivo .txt que quieres visualizar
    archivo_txt = st.file_uploader("Selecciona el archivo .txt ordenado", type=["txt"])

    if archivo_txt is not None:
        # Lee el contenido del archivo y decodifica en UTF-8
        contenido = archivo_txt.read().decode("utf-8", errors="replace")

        # Configura el ancho y alto del área de texto
        ancho = st.slider("Ancho del área de texto", 100, 700, 500)
        alto = st.slider("Alto del área de texto", 100, 800, 300)

        # Separar el contenido por etiquetas y agregar saltos de línea
        contenido_formateado = contenido.replace("Titulo", "\n\n**Titulo**").replace("Autor", "\n\n**Autor**") \
            .replace("Publicación", "\n\n**Publicación**").replace("Contenido", "\n\n**Contenido**") \
            .replace("Categoría", "\n\n**Categoría**").replace("URL", "\n\n**URL**").replace("Fuente", "\n\n**Fuente**") \
            .replace("Tipo de Fuente", "\n\n**Tipo de Fuente**")

        # Muestra el contenido en Streamlit con tamaño específico usando st.markdown
        st.markdown(
            f"<div style='width:{ancho}px; height:{alto}px; overflow:auto;'>"
            f"{contenido_formateado}</div>",
            unsafe_allow_html=True
        )

# Llama a la función principal
mostrar_contenido_txt()

st.divider()

