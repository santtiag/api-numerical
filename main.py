from fastapi import FastAPI, HTTPException, Query
import requests
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from models.urls import URL
from routers.differential_equation import differential_equation_router
from routers.interpolation import interpolation_router
from routers.regression import regression_router
from routers.definite_integration import definite_integration_router
from routers.methodology import methodology_router
from routers.auth import auth_router

app = FastAPI()
app.title = 'Numerical Project'

origins = [
    # "https://api-numerical.onrender.com", # render_url
    "http://localhost:3000", # localhost
    # "https://1faa-2800-e2-c180-5c6-00-2.ngrok-free.app" # ngrok_url
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    # allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["Content-Type", "Authorization"],
    max_age=3600,  # tiempo de vida de la configuración CORS (en segundos)
)

@app.get('/home', tags=['Home'])
async def print():
    return 'Hello πumerical'

app.include_router(interpolation_router)
app.include_router(regression_router)
app.include_router(definite_integration_router)
app.include_router(methodology_router)
app.include_router(differential_equation_router)
app.include_router(auth_router)
