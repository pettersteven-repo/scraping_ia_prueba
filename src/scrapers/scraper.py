from src.utils.helpers import obtener_html, extraer_hipervinculos, extraer_hipervinculos_categoria 
from src.config.settings import PAGINA, PAGINA_TEST

response = obtener_html(PAGINA_TEST)
hipervinculos_primer_nivel = extraer_hipervinculos(response)
lista_hipervinculos_interes = extraer_hipervinculos_categoria(hipervinculos_primer_nivel)