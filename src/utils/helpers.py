# Scrip para los metodos usados. 
from src.utils.logger import logger
from bs4 import BeautifulSoup
import requests


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
    
def extraer_hipervinculos(html):
    try:    
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")
        hipervinculos =[]
        logger.info("Se carga el codigo html y etiquetas de hipervinculo")
        for link in links:
            logger.info( f"Hipervinculo {link.get("href")} a la lista")
            if link.get("href") is not None and "e-commerce" in link.get("href"):
                hipervinculos.append(link.get("href"))    
        logger.info(f"Estos son los hipervinculos {hipervinculos}")
        return hipervinculos
    except BaseException as e:
        logger.error(f"Fallo al extraer hipervinculos {e}")
        raise ValueError(f"Fallo al extraer hipervinculos {e}")