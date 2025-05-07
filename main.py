# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Mi API Increíble",
    description="Una API de ejemplo que retorna cualquier cosa.",
    version="0.1.0" # Versión inicial de la API
)

@app.get("/")
async def root():
    """
    Endpoint raíz que retorna un saludo.
    """
    return {"message": "¡Hola desde mi API FastAPI!"}

@app.get("/test")
async def test():
    """
    Endpoint que retorna datos de ejemplo.
    """
    data = {
        "id": 12345,
        "nombre": "Objeto de Ejemplo",
        "descripcion": "Esto es solo un ejemplo para demostrar el API.",
        "activo": True,
        "tags": ["ejemplo", "api", "fastapi"]
    }
    return JSONResponse(content=data)

@app.get("/health")
async def health_check():
    """
    Endpoint de health check.
    """
    return {"status": "ok", "message": "API funcionando correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)