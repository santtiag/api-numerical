from fastapi.encoders import jsonable_encoder
import requests
from fastapi import APIRouter
from fastapi import Query
from fastapi.responses import JSONResponse

from models.const import URL_HOME, URL_REQ

interpolation_router = APIRouter()

@interpolation_router.get(URL_HOME.home.inter.lin_seg, tags=['Calculate Interpolation'])
async def calculate_i_lin_segm(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.inter.lin_seg, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)


@interpolation_router.get(URL_HOME.home.inter.quad_seg , tags=['Calculate Interpolation'])
async def calculate_i_quadratic_segm(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.inter.quad_seg, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)


@interpolation_router.get(URL_HOME.home.inter.cub_seg, tags=['Calculate Interpolation'])
async def calculate_i_cubic_segm(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.inter.cub_seg, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)
