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