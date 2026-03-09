from src.utils.logger import logger
from src.utils.helpers import obtener_html,  seleccionar_pagina_scraping
from src.scrapers.scraper import lista_hipervinculos_interes

from bs4 import BeautifulSoup
from src.config.settings import PAGINA


## clasificar los hipervinculos por categoria y tipo de categoria 

lista = lista_hipervinculos_interes

e_commerce = "allinone"
categoria =  "phones"
tipo_categoria = "touch"

url_scraping = seleccionar_pagina_scraping(e_commerce, categoria, tipo_categoria,lista_hipervinculos_interes)
try:    
    url_scraping = PAGINA + url_scraping
except ValueError("Subcategoria no esta en categoria"):
    raise ValueError("Subcategoria no esta en categoria")
#TypeError: can only concatenate str (not "NoneType") to str cuando el tipo_categoria no esta en la categoria 
print(url_scraping)


## Primer metodo de parsear alli
html_scraper = obtener_html(url_scraping)

soup = BeautifulSoup(html_scraper,"html.parser")
productos = soup.find_all("div", class_="col-md-4")

data = []

for producto in productos:
    nombre_producto = producto.find("a",class_="title").text.strip()
    precio_producto = producto.find("span", itemprop="price").text.strip()
    descripcion_producto = producto.find("p", class_="description").text.strip()
    reviews_porducto = producto.find("span", itemprop="reviewCount").text.strip()
    rating_producto = producto.find("p", attrs={"data-rating": True})["data-rating"]

    data.append(
        {
        "nombre" : nombre_producto,
        "precio" : precio_producto,
        "descripción" : descripcion_producto,
        "reviews" : reviews_porducto,
        "rating" : rating_producto
        }
    )
print(data)