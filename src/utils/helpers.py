# Scrip para los metodos usados. 
import sys
from src.config.settings import PAGINA
from src.utils.logger import logger
from bs4 import BeautifulSoup
import requests

#__________________________________________________________________________________#
# Función para scraper
def obtener_html(url):
    try:
        html= requests.get(url)
        logger.info(url)
        logger.info(html)
        if html.status_code == 200:
            return html.content
        else:
            logger.error(f"Pagina fallo error ")
            raise ValueError(f"{html.status_code}")
    except BaseException as e:
        logger.error(f"La pagina {url} no existe {e}")
        raise ValueError (f"La pagina {url} no existe {e}")
#__________________________________________________________________________________# 
# Funcipon de ubicación hipervinculos   
def extraer_hipervinculos(html):
    try:    
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")
        hipervinculos =[]
        logger.info("Se carga el codigo html y etiquetas de hipervinculo")
        for link in links:
            #logger.info( f"Hipervinculo {link.get("href")} a la lista")
            if link.get("href") is not None and "e-commerce" in link.get("href"):
                hipervinculos.append(link.get("href"))    
        logger.info(f"Estos son los hipervinculos ESTAN EN LA LISTA")
        return hipervinculos
    except BaseException as e:
        logger.error(f"Fallo al extraer hipervinculos {e}")
        raise ValueError(f"Fallo al extraer hipervinculos {e}")
#__________________________________________________________________________________#
# función ubicación hipervinculos    
def extraer_hipervinculos_categoria(lista):
    try:
        hipervinculos_segundo_nivel = []
        hipervinculos_tercer_nivel = []
        logger.info("Busqueda de hipervinculos de segundo nivel")
        for hiper in lista:
            url = PAGINA + hiper
            html = obtener_html(url=url)
            lista = [] 
            for link in extraer_hipervinculos(html=html):
                if link is not None and ("computers"in link or "phones" in link):
                    lista.append(link)
            hipervinculos_segundo_nivel.append(lista)
            logger.info("Se obtienen los hipervinculos de Categoria Phone y Computers")
        for lista_hiper in hipervinculos_segundo_nivel:
            logger.info("Se inicial proceso de obtención tipo categoria")
            for hiper_1 in lista_hiper:
                url_1 = PAGINA + hiper_1
                html_1 = obtener_html(url=url_1)
                #categorias = []
                for link_1 in extraer_hipervinculos(html_1):
                    #print(extraer_hipervinculos(html_1))
                    #print(link_1)
                    if link_1 is not None and ("laptops"in link_1 or "tablets" in link_1):
                        hipervinculos_tercer_nivel.append(link_1)
                    if link_1 is not None and "touch" in link_1:
                        hipervinculos_tercer_nivel.append(link_1)
                #hipervinculos_tercer_nivel.append(categorias)
            logger.info("Se obtienen los hipervinculos para tipo categoria")
        return hipervinculos_tercer_nivel
    except BaseException as e:
        logger.error(f"Fallo al extraer hipervinculos de categorias {e}")
        raise ValueError(f"Fallo al extraer hipervinculos de categorias {e}")
#__________________________________________________________________________________#
# Selección de hipervinculo a scrapear  
def seleccionar_pagina_scraping(e_commerce, categoria, tipo_categoria, lista):
    try:
        for link in lista:
            if e_commerce in link and categoria in link and tipo_categoria in link:
                return link
    except BaseException as e:
        logger.error("No se logra extraer el hipervinculo")
        raise ValueError("No se logra extraer el hipervinculo")
#__________________________________________________________________________________#
# Selección de hipervinculo a scrapear     

def pausa_usuario():
    opcion = input("\nScraping terminado. ¿Desea iniciar el análisis? (s/n): ").strip().lower()

    if opcion == "s":
        return True
    else:
        print("Programa detenido por el usuario.")
        sys.exit()