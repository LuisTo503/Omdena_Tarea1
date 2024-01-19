
import streamlit as st
from PIL import Image
#import cv2
import time
import numpy as np
from streamlit_extras.colored_header import colored_header

progress_text = "Cargando App..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

# st.button("Recargar")

st.sidebar.success("Elija una sección del proyecto")

st.title("¿Quiénes somos?")

st.divider()


def quienes_somos():

  col1, col2 = st.columns(2)
  with col1:

    colored_header(
          label="Nuestro equipo humano",
          description="",
          color_name="violet-70",
    )

    st.caption(" • Roxana Contreras")
    st.caption(" • Dionisia Escobar")
    st.caption(" • Carlos Hurtado")
    st.caption(" • Alicia Sánchez")
    st.caption(" • Luis Rolando Tobar")

  with col2:

    img=Image.open("asset\\nosotros.jpg")

    st.image(
          img,
          width=600,
          channels="RGB",
    )


st.subheader(
    "Somos un equipo de cinco profesionales comprometidos con el Data Science, uniendo nuestras habilidades")
st.subheader("y perspectivas diversas. Trabajamos colaborativamente para encontrar soluciones empresariales e institucionales")
st.subheader(
    "innovadoras y efectivas, fomentando un ambiente inclusivo donde cada voz cuenta.")
st.divider()


if __name__ == '__main__':
  quienes_somos()
