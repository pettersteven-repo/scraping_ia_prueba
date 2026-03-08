from src.utils.logger import logger
from src.utils.helpers import obtener_html, extraer_hipervinculos
from src.scrapers.scraper import hipervinculos_primer_nivel
from src.config.settings import PAGINA

# print(hipervinculos_primer_nivel)

# Extraer hipervinculos categoria
def extraer_hipervinculos_categoria(lista):
    hipervinculos_segundo_nivel = []
    logger.info("Busqueda de hipervinculos de segundo nivel")
    for hiper in lista:
        url = PAGINA + hiper
        html = obtener_html(url=url)
        lista = [] 
        for link in extraer_hipervinculos(html=html):
            if link is not None and ("computers"in link or "phones" in link):
                lista.append(link)
        hipervinculos_segundo_nivel.append(lista)
    return hipervinculos_segundo_nivel

tercer = extraer_hipervinculos_categoria(lista=hipervinculos_primer_nivel)
print(tercer)
