from src.utils.helpers import obtener_html, extraer_hipervinculos
from src.config.settings import PAGINA, PAGINA_TEST

response = obtener_html(PAGINA_TEST)
hipervinculos_primer_nivel = extraer_hipervinculos(response)