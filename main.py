from src.utils.logger import logger
from src.utils.helpers import obtener_html,  seleccionar_pagina_scraping
from src.scrapers.scraper import lista_hipervinculos_interes
from src.parsers.parsers import extraer_data_allinon

from bs4 import BeautifulSoup
from src.config.settings import PAGINA


## clasificar los hipervinculos por categoria y tipo de categoria 

lista = lista_hipervinculos_interes

e_commerce = "allinone"
categoria =  "phones"
tipo_categoria = "touch"

url_scraping = seleccionar_pagina_scraping(e_commerce, categoria, tipo_categoria,lista_hipervinculos_interes)



print(extraer_data_allinon(url_scraping))