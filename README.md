# Scraping IA

Este proyecto tiene como la presentación del proceso de selección a la vacante ______ Python. El proyecto se centra el la extracción, procesamiento y análisis de datos, haciendo uso de Web-Scraping e inteligencia artificial local. 

## Tecnologías Utilizadas

Este proyecto utiliza las siguientes herramientas y tecnologías:

 - Python 3
 - Requests – Para realizar solicitudes HTTP
 - BeautifulSoup – Para el análisis del HTML
 - Pandas – Manipulación y análisis de datos
 - Git y GitHub – Control de versiones

## Estructura del proyecto 
```
web-scraping-project
│
├── data
│   ├── raw                # Datos extraídos sin procesar
│   └── processed          # Datos limpios y transformados
│
├── notebooks              # Análisis exploratorio y pruebas
│
├── src                    # Código fuente del proyecto
│   ├── scraper            # Lógica de web scraping
│   │   └── scraper.py
│   │
│   ├── processing         # Limpieza y transformación de datos
│   │   └── preprocess.py
│   │
│   └── utils              # Funciones auxiliares
│       └── helpers.py
│
├── config                 # Archivos de configuración
│
├── tests                  # Pruebas del proyecto
│
├── requirements.txt       # Dependencias del proyecto
│
├── README.md              # Documentación del proyecto
│
└── main.py                # Script principal de ejecución
```