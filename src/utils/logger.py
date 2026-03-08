import logging

def setup_logger():
    logger = logging.getLogger("logs")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    )

    file_handler = logging.FileHandler("logs/scraper.log")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

if __name__ == "__main__":
    logger.info("Logger cargado correctamente.")
    logger.error("Logger Error.")
    logger.warning("Este es un mensaje de advertencia para propósitos de prueba.")
