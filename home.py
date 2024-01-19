
import streamlit as st 
from PIL import Image
import cv2
import time
from streamlit_embedcode import github_gist
from streamlit.elements.image import Channels
from streamlit_player import st_player

progress_text = "Cargando App..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()





def main():

  st.title("Proyecto Final")
  st.subheader("Desarrollo de un Sistema de Análisis de Noticias ")
  st.subheader(" del portal:  https://www.ultimahora.sv")
  st.divider()
  st.sidebar.success("Elija una sección del proyecto")
  

  img=Image.open("asset\\oficinistas.jpg")
  st.image(
    img, 
    width=1080,
    channels="RGB",
  )

  
  st.divider()
  st.subheader("Presentación del proyecto")
  st.write("")
  
  st_player("https://youtu.be/JB0z_-Pqp7M") 
  
  
  st.divider()
  
  st.subheader("Script del proyecto")
  github_gist(
      "https://github.com/LuisRTobar/18.04.24_Omdena_Tarea1_DataScience.git",
      width=1080,
      height=800,
  )
  
  st.divider()
  
  st.caption("enlace del proyecto: https://github.com/LuisRTobar/Tarea_Omdena_final.git")


if __name__ == '__main__':
  main()


