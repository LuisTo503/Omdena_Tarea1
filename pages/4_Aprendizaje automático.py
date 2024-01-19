
import streamlit as st 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

from sklearn.metrics import roc_curve, auc
import seaborn as sns
import matplotlib.pyplot as plt


st.title("4. Aprendizaje automático")

# Cargar los datos desde el archivo CSV
url = "data\\Noticias_Ultima_Hora.csv"
data = pd.read_csv(url)

# 
X = data['title'] + ' ' + data['content']
y = data['category_id']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo TF-IDF y un clasificador Naive Bayes
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Hacer predicciones en nuevos datos
def predict_sentiment(text):
    text_tfidf = tfidf_vectorizer.transform([text])
    prediction = model.predict(text_tfidf)
    return prediction[0]

# Interfaz de usuario con Streamlit
st.title("Análisis de Sentimiento con Aprendizaje Automático")

text_input = st.text_area("Introduce un texto para análisis de sentimiento:", "")
if st.button("Predecir"):
    prediction = predict_sentiment(text_input)
    st.write(f"Sentimiento Predicho: {prediction}")

# Evaluación del modelo
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)

st.subheader("Evaluación del Modelo")
st.write(f"Precisión del Modelo: {accuracy:.2%}")
st.write("Informe de Clasificación:")
st.text(classification_report(y_test, y_pred))

