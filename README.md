# Nombre de tu Proyecto
    Desarrollo de un Sistema de Análisis de Noticias Salvadoreñas. Especificamente del portal: https://ultimahora.sv/
## Descripción
    El objetivo principal de este proyecto es aplicar los fundamentos de ciencia de datos para desarrollar un sistema integral de análisis de noticias salvadoreñas. Se abordarán diferentes etapas, desde la obtención de datos mediante web scraping hasta la implementación de modelos de aprendizaje automático y procesamiento del lenguaje natural, culminando con la creación de una interfaz interactiva utilizando Streamlit.
    https://github.com/LuisRTobar/18.04.24_Omdena_Tarea1_DataScience.git


## Requisitos
    instalar archivo: requirements.txt
    `pip install -r requirements.txt`


## Instalación
1. Clona el repositorio: `git clone https://github.com/LuisRTobar/18.04.24_Omdena_Tarea1_DataScience.git  
2. Accede al directorio: `cd tu_proyecto`
3. Crea un entorno virtual: `python -m venv venv`
4. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En Linux/Mac: `source venv/bin/activate`
5. Instala las dependencias: `pip install -r requirements.txt`
.
6. Usar el Archivo requirements.txt en Otro Entorno:
Para recrear las mismas condiciones en otro entorno, puedes crear un nuevo entorno virtual y luego instalar las bibliotecas desde el archivo requirements.txt
    `python -m venv nuevo_entorno`
    `nuevo_entorno\Scripts\activate`  o 
    `source nuevo_entorno/bin/activate` en macOS/Linux
    `pip install -r requirements.txt`

**Conación de repositorio de GitHub**
    `echo "# 18.04.24_Ondema_Tarea1_DataScience" >> README.md`
    `git init`
    `git add README.md`
    `git commit -m "first commit"`
   `git branch -M main`
    `git remote add origin https://github.com/LuisRTobar/18.04.24_Omdena_Tarea1_DataScience.git`
    `git push -u origin main`
**o enviar un repositorio existente desde la línea de comandos**
    `git remote add origin https://github.com/LuisRTobar/18.04.24_Omdena_Tarea1_DataScience.git`
   `git branch -M main`
    `git push -u origin main`

## Uso desde la carpeta raíz
1. `streamlit run home.py`
ejemplo practico en el siguiente enlace al video:

## Estructura de Carpetas
- asset/:  "contiene archivos de imagenes utilizadas en el DOM del proyecto"
- notebooks/: Incluye cuaderno Jupyter- Google Colab, utilizados para:      Web Scraping, análisis exploratorio de datos (EDA), procesamiento NLP, aprendizaje automático y experimentación.
- pages/: Incluye los script a las distintas páginas web para visualizarse en el framework de Streamlit y los archivos y sus funciones son:
    [1_Web_scraping.py]: Incluye scripts y módulos específicos para la visualización de los datos obtenidos mediante técnicas de web scraping utilizados en el cuadernno de Colab.
    [2_Analisis_EDA.py]: nos muestra en distintas presentaciones interactivas 



## Contribución
Este proyecto te puede servir de base para analisis y visualizar otros portales de noticias, los cuales deberás de modificar sus "etiquetas" del DOM de cada web y sustituirlas en el Jupiter o Colab y experimentar, hasta lograr buenos resultados.

## Licencia
Licencia MIT, descrita en el archivo LICENSE.md
