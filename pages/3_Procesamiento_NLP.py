
import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import spacy
from spacy import displacy
from textblob import TextBlob
import seaborn as sns

import nltk
nltk.download('punkt')
# Cargar el modelo en español
nlp = spacy.load("es_core_news_sm")

st.title("3. Procesamiento del Lenguaje Natural (NLP)")

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Cargar datos desde el archivo CSV
url = "data\\Noticias_Ultima_Hora.csv"
data = pd.read_csv(url)

# Texto explicativo sobre lematización y etiquetado gramatical
texto_explicativo = """
## Lematización y Etiquetado Gramatical

La **lematización** es un proceso en el que las palabras se reducen a su forma base o lema. 
El lema es la forma canónica de una palabra y representa su significado básico. 
Por ejemplo, la lematización convertiría "corriendo" a "correr" o "ratones" a "ratón".

El **etiquetado gramatical** es el proceso de asignar a cada palabra en un texto una etiqueta que indica su categoría gramatical. 
Estas categorías incluyen sustantivos, verbos, adjetivos, etc. 
Por ejemplo, en la frase "El gato está durmiendo", el etiquetado gramatical asignaría "sustantivo" a "gato", "verbo" a "está", y "gerundio" a "durmiendo".

Ambas técnicas son esenciales en procesamiento de lenguaje natural para comprender y analizar textos de manera más efectiva.

En esta aplicación, utilizamos la lematización y el etiquetado gramatical para procesar el texto seleccionado y obtener una representación más significativa de las palabras.
"""

# Mostrar el texto explicativo en Streamlit
st.markdown(texto_explicativo)

# Seleccionar columna de texto
columna_texto = st.sidebar.selectbox("Seleccionar columna de texto", ["title", "content"])

# Obtener el texto de la columna seleccionada
texto = " ".join(data[columna_texto].dropna())

# Procesamiento de Texto
st.header("Procesamiento de Texto en la columna '{}'".format(columna_texto))

# Dividir la pantalla en 3 columnas
col1, col2, col3 = st.columns(3)

# Columna 1: Texto Original
with col1:
    st.subheader("Texto Original:")
    st.write(texto)

# Columna 2: Tokenización
with col2:
    st.subheader("Tokenización:")
    tokens = word_tokenize(texto)
    st.write(tokens)

# Columna 3: Lematización y Etiquetado Gramatical
with col3:
    st.subheader("Lematización y Etiquetado Gramatical:")
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word) for word in tokens]
    pos_tags = pos_tag(tokens)
    st.write({"Lematización": lemmas, "Etiquetado Gramatical": pos_tags})

# Mostrar Gráfico de WordCloud
st.header("WordCloud de la columna '{}'".format(columna_texto))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

#

# Cargar modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

# Función para realizar análisis de sentimientos
def analisis_sentimientos(texto):
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    subjetividad = blob.sentiment.subjectivity
    return polaridad, subjetividad

# Función para realizar extracción de entidades
def extraccion_entidades(texto):
    doc = nlp(texto)
    entidades = [ent.text for ent in doc.ents]
    return entidades

# Función para realizar clasificación de texto (dummy, solo como ejemplo)
def clasificacion_texto(texto):
    # Aquí puedes implementar un modelo de clasificación real
    # En este caso, simplemente clasificamos como "Positivo" o "Negativo" según la polaridad del análisis de sentimientos
    polaridad, _ = analisis_sentimientos(texto)
    if polaridad >= 0:
        return "Positivo"
    else:
        return "Negativo"

# Cargar datos desde el archivo CSV
url = "data\\Noticias_Ultima_Hora.csv"

st.title("")
st.divider()


# Función para realizar análisis de sentimientos y devolver la categoría (negativo, neutro, positivo)
def analisis_sentimientos(texto):
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    
    if polaridad < 0:
        return "Negativo"
    elif polaridad == 0:
        return "Neutro"
    else:
        return "Positivo"

# Realizar análisis de sentimientos para las columnas "title" y "content"
data['sentimiento_title'] = data['title'].apply(analisis_sentimientos)
data['sentimiento_content'] = data['content'].apply(analisis_sentimientos)

# Crear dos columnas para los gráficos
col1, col2 = st.columns(2)

# Gráfico de barras para "title"
with col1:
    st.subheader("Análisis de Sentimientos en Títulos")
    fig_title = plt.figure()
    sns.countplot(x='sentimiento_title', data=data, order=['Negativo', 'Neutro', 'Positivo'])
    plt.xlabel('Sentimiento')
    plt.ylabel('Cantidad')
    st.pyplot(fig_title)

# Gráfico de barras para "content"
with col2:
    st.subheader("Análisis de Sentimientos en Contenidos")
    fig_content = plt.figure()
    sns.countplot(x='sentimiento_content', data=data, order=['Negativo', 'Neutro', 'Positivo'])
    plt.xlabel('Sentimiento')
    plt.ylabel('Cantidad')
    st.pyplot(fig_content)
    

