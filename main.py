from fastapi import FastAPI, HTTPException, Query
import requests
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from models.urls import URL

app = FastAPI()
app.title = 'Numerical Project'

origins = [
    # "https://api-numerical.onrender.com", # render_url
    "http://localhost:3000", # localhost
    "https://1faa-2800-e2-c180-5c6-00-2.ngrok-free.app" # ngrok_url
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

url = URL('/home')
# INFO: The path that u need to change to the ulr -> 'url_ngrok/engine/'
url_req = URL('https://engine-numerical.onrender.com/engine')
# url_req = 'https://efe9-2803-1800-11c4-4541-cd84-4b70-7f0c-ae3a.ngrok-free.app/engine/'

@app.get('/home', tags=['Home'])
async def print():
    return 'Hello πumerical'


# INFO: <-- INTERPOLATION -->
@app.get(url.home.inter.quad_seg , tags=['Calculate Interpolation'])
async def calculate_i_quadratic_segm(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(url_req.home.inter.quad_seg, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)


@app.get(url.home.inter.cub_seg, tags=['Calculate Interpolation'])
async def calculate_i_cubic_segm(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(url_req.home.inter.cub_seg, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)


# INFO: <-- REGRESSION -->
@app.get(url.home.reg.lin, tags=['Calculate Regression'])
async def calculate_r_linear(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(url_req.home.reg.lin, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')

@app.get(url.home.reg.nonlin.exp, tags=['Calculate Regression'])
async def calculate_r_nonlinear_exponential(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(url_req.home.reg.nonlin.exp, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')


@app.get(url.home.reg.nonlin.pot, tags=['Calculate Regression'])
async def calculate_r_nonlinear_potential(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(url_req.home.reg.nonlin.pot, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')


@app.get(url.home.reg.nonlin.poly, tags=['Calculate Regression'])
async def calculate_r_nonlinear_polynomial(x: str = Query(...), y: str = Query(...), n: int = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values, 'n': n}

    response = requests.post(url_req.home.reg.nonlin.poly, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')
