from src.utils.logger import logger #
from src.utils.helpers import seleccionar_pagina_scraping
from src.scrapers.scraper import lista_hipervinculos_interes
from src.parsers.parsers import extraer_data_allinon, extraer_data_static, guardar_cvs
from src.pipelines.ia_analisis import cargar_datos, limpiar_dataframe, generar_resumen, crear_prompt_resumen,crear_prompt_anomalias,consultar_modelo, guardar_analisis

import pandas as pd
import ollama
#############################################################################################
# Variables prueba

e_commerce = "static" 
categoria = "phones"
tipo_categoria = "touch"
numero_paginas = 1

# def solicitar_variables():
#     while True:
#         e_commerce = input("Seleccione el tipo de e-commerce (allinone / static): ").lower()
#         if e_commerce in ["allinone", "static"]:
#             break
#         else:
#             print("Valor inválido. Opciones: allinone o static")
#     while True:
#         categoria = input("Seleccione la categoría (computers / phones): ").lower()
#         if categoria in ["computers", "phones"]:
#             break
#         else:
#             print("Valor inválido. Opciones: computers o phones")
#     if categoria == "computers":
#         while True:
#             tipo_categoria = input("Seleccione tipo de categoría (laptops / tablets): ").lower()
#             if tipo_categoria in ["laptops", "tablets"]:
#                 break
#             else:
#                 print("Valor inválido. Opciones: laptops o tablets")
#     else:
#         tipo_categoria = "touch"
#         print("Tipo de categoría asignado automáticamente:", tipo_categoria)
#     numero_paginas = 1
#     if e_commerce == "static":
#         while True:
#             try:
#                 numero_paginas = int(input("Ingrese el número de páginas a scrapear: "))
#                 if numero_paginas > 0:
#                     break
#                 else:
#                     print("El número debe ser mayor que 0")
#             except ValueError:
#                 print("Ingrese un número válido")
#     return e_commerce, categoria, tipo_categoria, numero_paginas

# e_commerce, categoria, tipo_categoria, numero_paginas = solicitar_variables()

#############################################################################################
# scraping 

print("\nValores seleccionados:")
print("e_commerce:", e_commerce)
print("categoria:", categoria)
print("tipo_categoria:", tipo_categoria)
print("numero_paginas:", numero_paginas)

url_scraping = seleccionar_pagina_scraping(e_commerce, categoria, tipo_categoria,lista_hipervinculos_interes)

data = []
if e_commerce == "allinone":
    data =  extraer_data_allinon(url_scraping) 
elif e_commerce == "static":
    data = extraer_data_static(url_scraping,numero_paginas)
else:
    logger.error("No se tiene DATOS")

print(data)
guardar_cvs(e_commerce,categoria,tipo_categoria,numero_paginas,data)

#############################################################################################
# IA

dataframe = cargar_datos(e_commerce, categoria, tipo_categoria, numero_paginas)
dataframe = limpiar_dataframe(dataframe)
contexto = generar_resumen(dataframe)

prompt1 = crear_prompt_resumen(contexto)
prompt2 = crear_prompt_anomalias(contexto)

respuesta_resumen = consultar_modelo(prompt1)
respuesta_anomalias = consultar_modelo(prompt2)

guardar_analisis(respuesta_resumen,respuesta_anomalias)