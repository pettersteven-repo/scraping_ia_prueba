import pandas as pd
from bs4 import BeautifulSoup
from src.config.settings import PAGINA
from src.utils.logger import logger
from src.utils.helpers import obtener_html

def extraer_data_allinon(url_scraping):
    try:    
        url_scraping = PAGINA + url_scraping
        logger.info("Se obtine hipervinculo para pagina a parsear")
    except ValueError("Error en los parametros!!!"):
        raise ValueError("Error en los parametros!!!")
    
    html_scraper = obtener_html(url_scraping)
    soup = BeautifulSoup(html_scraper,"html.parser")
    # Busqueda de recuadros con información del producto
    productos = soup.find_all("div", class_="col-md-4")

    try:
        data = []
        for producto in productos:
            nombre_producto = producto.find("a",class_="title").text.strip()
            precio_producto = producto.find("span", itemprop="price").text.strip()
            descripcion_producto = producto.find("p", class_="description").text.strip()
            reviews_porducto = producto.find("span", itemprop="reviewCount").text.strip()
            rating_producto = producto.find("p", attrs={"data-rating": True})["data-rating"]

            data.append(
                {
                "nombre" : nombre_producto,
                "precio" : precio_producto,
                "descripción" : descripcion_producto,
                "reviews" : reviews_porducto,
                "rating" : rating_producto
                }
            )
        return data
    except BaseException as e:
        logger.error("No se pudo obtener la información")
        raise("No se pudo obtener la información")
    
def extraer_data_static(url_scraping,numero_paginas):
    url_page = "?page="
    try:
        data_static = []
        for i in range(numero_paginas):
            url_page_numero = url_scraping + url_page + str(i+1)
            data_page = extraer_data_allinon(url_page_numero)
            data_static.extend(data_page)
        logger.info(f"Se extrae información de las {numero_paginas} paginas")
        return data_static
    except BaseException as e:
        logger.error("No se pudo extraer los datos de static")
        raise("No se pudo extraer los datos de static")    
    

def guardar_cvs(e_commerce, categoria, tipo_categoria, numero_paginas, data):
    try:
        datos = pd.DataFrame(data)
        if numero_paginas == 1:
            nombre_archivo = f"data/{e_commerce}_{categoria}_{tipo_categoria}.csv"
        else:
            nombre_archivo = f"data/{e_commerce}_{categoria}_{tipo_categoria}_pag{numero_paginas}.csv"
        datos.to_csv(nombre_archivo, encoding="utf-8")
        logger.info(f"Datos guardados en CSV: {nombre_archivo}")
    except Exception as e:
        logger.error("No se guardó el CSV")
        raise Exception("No se guardó el CSV") from e