from src.utils.logger import logger
from src.utils.helpers import obtener_html, extraer_hipervinculos, extraer_hipervinculos_categoria
from src.scrapers.scraper import hipervinculos_primer_nivel

tercer = extraer_hipervinculos_categoria(lista=hipervinculos_primer_nivel)

print(tercer)
