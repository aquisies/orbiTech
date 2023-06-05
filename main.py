from fastapi import FastAPI, Request
from app.utils.logging import setup_logging
from app.api.endpoints import router as endpoints_router
from app.database.connection import get_db
from dotenv import load_dotenv

# Aplicación FastAPI
app = FastAPI()

load_dotenv()

app.include_router(endpoints_router)

# Configuración del router principal de los endpoints
@app.get("/")
async def welcome():
    return {"message": "Bienvenido a mi aplicación"}


# Configurar el middleware para llamar a setup_logging antes de cada solicitud
@app.middleware("http")
async def setup_logging_middleware(request: Request, call_next):
    setup_logging(request)  # Llamar a setup_logging antes de procesar la solicitud
    response = await call_next(request)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
