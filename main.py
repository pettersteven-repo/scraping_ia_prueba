from src.utils.logger import logger
from src.utils.helpers import obtener_html, extraer_hipervinculos
from src.scrapers.scraper import hipervinculos_primer_nivel
from src.config.settings import PAGINA

print(hipervinculos_primer_nivel)

hipervinculos_segundo_nivel = []
hipervinculos_tercer_nivel = []
logger.info("INICIA SEGUNDO NIIVEL __________________________________________________________________")
for hiper in [hipervinculos_primer_nivel[0]]:
    url = PAGINA + hiper
    html = obtener_html(url=url)
    lista = extraer_hipervinculos(html=html)
    hipervinculos_segundo_nivel.append(lista)
for hiper in hipervinculos_segundo_nivel:
    for hiper_2 in hiper:
        url_2 = PAGINA + hiper_2
        html_2 = obtener_html(url=url_2)
        lista_2 = extraer_hipervinculos(html=html_2)
        hipervinculos_tercer_nivel.append(lista_2)

print(hipervinculos_tercer_nivel)
