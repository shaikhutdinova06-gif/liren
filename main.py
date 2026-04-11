import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Fix OpenMP runtime conflict
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.api.routes import router
from backend.api.calculator import router as calculator_router
from config import logger

app = FastAPI(title="Liren Bot - Soil Classification System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api")
app.include_router(calculator_router, prefix="/api")

# Serve static files
app.mount("/static", StaticFiles(directory="frontend", html=True), name="static")

@app.get("/")
async def root():
    from fastapi.responses import HTMLResponse
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/health")
async def health_check():
    return {"status": "healthy", "soil_classifier": "ready"}

if __name__ == "__main__":
    logger.info("Starting Liren Bot server...")
    logger.info("Frontend available at: http://localhost:8000/static")
    logger.info("API documentation at: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
