from src.utils.logger import logger
from src.scrapers.scraper import response
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("a")
hipervinculos =[]
for link in links:
    if link.get("href") is not None and "e-commerce" in link.get("href"):
        hipervinculos.append(link.get("href"))


print(hipervinculos)
