import ollama
import pandas as pd
from src.utils.logger import logger

def cargar_datos(e_commerce,  categoria, tipo_categoria, numero_paginas):
    path = ""
    if numero_paginas == 1:
            path = f"data/{e_commerce}_{categoria}_{tipo_categoria}.csv"
    else:
        path = f"data/{e_commerce}_{categoria}_{tipo_categoria}_{numero_paginas}pag.csv"
    df = pd.read_csv(path)

    return df

def limpiar_dataframe(dataframe):
    try:
        dataframe["precio"] = dataframe["precio"].str.replace("$", "", regex=False).astype(float)
        dataframe["reviews"] = dataframe["reviews"].astype(int)
        dataframe["rating"] = dataframe["rating"].astype(int)
        logger.info("Se limpian datos del dataframe")
    except BaseException as e:
        logger.error("No se pueden limpiar los datos del dataframe")
        raise("No se pueden limpiar los datos del dataframe")
    return dataframe

def generar_resumen(dataframe):
    try:
        total_productos = len(dataframe)
        precio_promedio = dataframe["precio"].mean()
        rating_promedio = dataframe["rating"].mean()
        top_productos = dataframe.head(5)
        resumen = f"""

        Ejemplo de productos:
        {top_productos}

        
        Total productos vistos: {total_productos}
        Precio promedio: {precio_promedio}
        Rating promedio: {rating_promedio}
        
        """
        logger.info("Se genera resumen datos")
        return resumen
    except BaseException as e:
        logger.error("No se genera resumen")
        raise("No se genera resumen")

def crear_prompt_resumen(contexto):
    try:
        prompt = f"""
        Analiza el siguiente dataset de productos de e-commerce.

        {contexto}

        Resume los resultados obtenidos.
        """
        logger.info("Se crea Prompt")
        return prompt
    except BaseException as e:
        logger.error("no se puede crear Prompt")

def crear_prompt_anomalias(contexto):
    prompt = f"""
    Analiza los datos del dataset.

    {contexto}

    Identifica posibles anomalías en precios o ratings.
    """
    return prompt

def consultar_modelo(prompt):

    respuesta = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta["message"]["content"]

def guardar_analisis(resumen, anomalias):

    with open("output/ai_summary.md", "w", encoding="utf-8") as f:

        f.write("# Análisis del Dataset\n\n")

        f.write("## Resumen\n")
        f.write(resumen)

        f.write("\n\n## Anomalías detectadas\n")
        f.write(anomalias)