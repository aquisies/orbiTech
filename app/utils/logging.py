import logging
from fastapi import  Request

def setup_logging(request: Request):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="app.log",  # Nombre del archivo de registro
        filemode="a"  
    )

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)

    logger.info("Logger OK.")
    print("ruta:",request.url)
    
# setup_logging()
