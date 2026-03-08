# Scrip para los metodos usados.

from src.utils.logger import logger
import requests

def obtener_html(url):
    try:
        html= requests.get(url)
        logger.info(url)
        logger.info(html)
        if html.status_code == 200:
            return html
        else:
            logger.error(f"Pagina fallo error ")
            raise ValueError(f"{html.status_code}")
    except BaseException as e:
        logger.error(f"La pagina {url} no existe {e}")