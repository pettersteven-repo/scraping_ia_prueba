from dotenv import load_dotenv 
import os
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Leer varianles de entorno
PAGINA = os.getenv('pagina')


