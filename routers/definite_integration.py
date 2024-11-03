from fastapi import APIRouter, HTTPException
from fastapi import Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests

from models.const import URL_HOME, URL_REQ


definite_integration_router = APIRouter()
@definite_integration_router.get(URL_HOME.home.d_i.rect,tags=['Definite Integration'])
async def calculate_di_rectangle(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.d_i.rect, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')


@definite_integration_router.get(URL_HOME.home.d_i.trap, tags=['Definite Integration'])
async def calculate_di_trapezium(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.d_i.trap, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')


@definite_integration_router.get(URL_HOME.home.d_i.para, tags=['Definite Integration'])
async def calculate_di_parabola(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.d_i.para, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')


@definite_integration_router.get(URL_HOME.home.d_i.ca, tags=['Definite Integration'])
async def calculate_di_cubic_definite_integration_routerroximation(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.d_i.ca, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')
