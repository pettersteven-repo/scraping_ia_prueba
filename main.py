from src.utils.logger import logger #
from src.utils.helpers import seleccionar_pagina_scraping, pausa_usuario, solicitar_variables
from src.scrapers.scraper import lista_hipervinculos_interes
from src.parsers.parsers import extraer_data_allinon, extraer_data_static, guardar_cvs
from src.pipelines.ia_analisis import cargar_datos, limpiar_dataframe, generar_resumen, crear_prompt_resumen,crear_prompt_anomalias,consultar_modelo, guardar_analisis

###########################################################################
 
# Variables prueba
# e_commerce = "static" 
# categoria = "phones"
# tipo_categoria = "touch"
# numero_paginas = 1

e_commerce, categoria, tipo_categoria, numero_paginas = solicitar_variables()

#############################################################################################
# scraping 

print("\nValores seleccionados:")
print("e_commerce:", e_commerce)
print("categoria:", categoria)
print("tipo_categoria:", tipo_categoria)
print("numero_paginas:", numero_paginas)
print("\n")

url_scraping = seleccionar_pagina_scraping(e_commerce, categoria, tipo_categoria,lista_hipervinculos_interes)

data = []
if e_commerce == "allinone":
    data =  extraer_data_allinon(url_scraping) 
elif e_commerce == "static":
    data = extraer_data_static(url_scraping,numero_paginas)
else:
    logger.error("No se tiene DATOS")

#print(data)
guardar_cvs(e_commerce,categoria,tipo_categoria,numero_paginas,data)

print("El documento ha sido creado")
pausa_usuario()

#############################################################################################
# IA

dataframe = cargar_datos(e_commerce, categoria, tipo_categoria, numero_paginas)
dataframe = limpiar_dataframe(dataframe)
print(dataframe)
contexto = generar_resumen(dataframe)

prompt1 = crear_prompt_resumen(contexto)
prompt2 = crear_prompt_anomalias(contexto)

respuesta_resumen = consultar_modelo(prompt1)
respuesta_anomalias = consultar_modelo(prompt2)

guardar_analisis(respuesta_resumen,respuesta_anomalias, e_commerce, categoria, tipo_categoria,numero_paginas)

