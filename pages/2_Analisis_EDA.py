
import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import seaborn as sns
from wordcloud import WordCloud
import wordcloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PIL import Image
import nltk
nltk.download('stopwords')
nltk.download('punkt')


# URL del archivo CSV en GitHub
url = "data\\Noticias_Ultima_Hora.csv"

# Cargar datos desde el archivo CSV
data = pd.read_csv(url)

# Título de la página
st.title("2. Análisis Exploratorio de Datos (EDA)")

# Sidebar para opciones interactivas
st.sidebar.subheader("Opciones Interactivas")

# Widget interactivo para seleccionar columna, con "category_id" como valor predeterminado
columna_seleccionada = st.sidebar.selectbox(
    "Seleccionar Columna", data.columns, index=data.columns.get_loc("category_id"))

# Verificar si la columna seleccionada es categórica
if data[columna_seleccionada].dtype == 'O':
    # Contar el número de noticias por cada categoría
    conteo_por_categoria = data[columna_seleccionada].value_counts()

    # Visualizar el número de noticias por cada categoría
    st.subheader("Conteo de Noticias por Categoría")
    st.bar_chart(conteo_por_categoria)

    # Mostrar tabla con el conteo
    st.subheader("Tabla del conteo de Noticias por Categoría")
    st.table(conteo_por_categoria)
    st.divider()

    # Estadísticas descriptivas
    st.subheader("Estadísticas Descriptivas")
    st.write(data[columna_seleccionada].describe())

    # Gráfico de pastel
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(conteo_por_categoria, labels=conteo_por_categoria.index,
               autopct='%1.1f%%', startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax_pie.axis('equal')
    st.pyplot(fig_pie)
    st.divider()


# Sidebar para opciones interactivas
st.sidebar.subheader("Opciones Interactivas")
columna_seleccionada = st.sidebar.selectbox(
    "Seleccionar Columna", data.columns)

# Verificar si la columna seleccionada es categórica
if data[columna_seleccionada].dtype == 'O':
    # Título de la página
    st.title("Histograma por Categoría")

    # Crear una figura más grande y ejes
    fig_hist, ax_hist = plt.subplots(figsize=(12, 6))

    # Configurar el estilo del gráfico
    sns.set(style="whitegrid")
    sns.set_palette("pastel")

    # Crear el histograma
    for categoria in data[columna_seleccionada].unique():
        sns.histplot(data[data[columna_seleccionada] == categoria]
                     ['category_id'], label=categoria, kde=False, ax=ax_hist)

    # Ajustar el formato del eje x
    ax_hist.set_xticklabels(ax_hist.get_xticklabels(
    ), rotation=45, horizontalalignment='right', fontsize='small')

    # Añadir título y leyenda
    plt.title('Histograma por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Frecuencia')
    plt.legend(title='Categorías', loc='upper right')

    # Mostrar el gráfico interactivo
    st.pyplot(fig_hist)

st.divider()

# --- NUBE DE PALABRAS por titulo---

# Título de la página
st.title("Nube de Palabras más frecuentes - en 'Títulos' de las noticias")
st.title("")

# Concatenar todos los textos en una única cadena
text = " ".join(data['title'].dropna())

# Tokenizar las palabras y eliminar las palabras vacías
stop_words = set(stopwords.words('spanish'))
words = word_tokenize(text)
filtered_words = [word.lower() for word in words if word.isalnum()
                  and word.lower() not in stop_words]

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(
    " ".join(filtered_words))

# Mostrar la nube de palabras usando st.image()
st.image(wordcloud.to_array(), width=800)


# Título de la página
st.title("Tabla de la frecuencia de las palabras en los Títulos de las Noticias")
st.title("")

# Concatenar todos los textos en una única cadena
text_content = " ".join(data['title'].dropna())

# Tokenizar las palabras y eliminar las palabras vacías
stop_words = set(stopwords.words('spanish'))
words_content = word_tokenize(text_content)
filtered_words_content = [word.lower(
) for word in words_content if word.isalnum() and word.lower() not in stop_words]

# Contar la frecuencia de cada palabra
word_freq = pd.Series(filtered_words_content).value_counts()

# Crear un DataFrame con las palabras y su frecuencia
df_word_freq = pd.DataFrame(
    {"Palabra": word_freq.index, "Frecuencia": word_freq.values})

###

###
# Agregar un slider para ajustar el número de filas mostradas
num_rows = st.slider("Número de Filas a Mostrar", 10, 100, 10)

# Mostrar el DataFrame con el número de filas seleccionado
st.subheader(
    "Palabras más Frecuentes y su Frecuencia en los Títulos de las Noticias")
st.table(df_word_freq.head(num_rows))
#
#
#
# --- GRÁFICO DE PASTEL PARA LOS TÍTULOS ---
st.subheader("Gráfico de Pastel para Palabras más Frecuentes en Títulos")

# Grafico de pastel
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(df_word_freq['Frecuencia'][:num_rows],
           labels=df_word_freq['Palabra'][:num_rows], autopct='%1.1f%%', startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle.
ax_pie.axis('equal')
st.pyplot(fig_pie)
#


st.divider()


#
# --- NUBE DE PALABRAS por contenido ---
# Título de la página
st.title("Nube de Palabras más frecuentes - en 'Contenido' de las noticias")
st.title("")

# Concatenar todos los textos en una única cadena
text = " ".join(data['content'].dropna())

# Tokenizar las palabras y eliminar las palabras vacías
stop_words = set(stopwords.words('spanish'))
words = word_tokenize(text)
filtered_words = [word.lower() for word in words if word.isalnum()
                  and word.lower() not in stop_words]

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(
    " ".join(filtered_words))

# Mostrar la nube de palabras usando st.image()
st.image(wordcloud.to_array(), width=800)


# --- TABLA DE FRECUENCIA DE PALABRAS ---
# Título de la página
st.title("Tabla de la frecuencia de las palabras en los contenidos de las noticias")
st.title("")

# Concatenar todos los textos en una única cadena
text_content = " ".join(data['content'].dropna())

# Tokenizar las palabras y eliminar las palabras vacías
stop_words = set(stopwords.words('spanish'))
words_content = word_tokenize(text_content)
filtered_words_content = [word.lower(
) for word in words_content if word.isalnum() and word.lower() not in stop_words]

# Contar la frecuencia de cada palabra
word_freq = pd.Series(filtered_words_content).value_counts()

# Crear un DataFrame con las palabras y su frecuencia
df_word_freq = pd.DataFrame(
    {"Palabra": word_freq.index, "Frecuencia": word_freq.values})

# Agregar un slider para ajustar el número de filas mostradas
num_rows = st.slider("Número de Filas a Mostrar", 10,
                     100, 10, key="slider_unique_key")

# Mostrar el DataFrame con el número de filas seleccionado
st.subheader(
    "Palabras más Frecuentes y su Frecuencia en los Contenidos de las Noticias")
st.table(df_word_freq.head(num_rows))

# --- GRÁFICO DE PASTEL ---
st.subheader(
    "Gráfico de Pastel de Palabras más Frecuentes en los Contenidos de las Noticias")
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(df_word_freq["Frecuencia"].head(num_rows),
           labels=df_word_freq["Palabra"].head(num_rows), autopct='%1.1f%%', startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle.
ax_pie.axis('equal')
st.pyplot(fig_pie)
