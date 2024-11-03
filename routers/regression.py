
from fastapi import HTTPException, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter
import requests
from models.const import URL_HOME, URL_REQ

regression_router = APIRouter()

@regression_router.get(URL_HOME.home.reg.lin, tags=['Calculate Regression'])
async def calculate_r_linear(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.reg.lin, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')

@regression_router.get(URL_HOME.home.reg.nonlin.exp, tags=['Calculate Regression'])
async def calculate_r_nonlinear_exponential(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.reg.nonlin.exp, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')


@regression_router.get(URL_HOME.home.reg.nonlin.pot, tags=['Calculate Regression'])
async def calculate_r_nonlinear_potential(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(URL_REQ.home.reg.nonlin.pot, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')


@regression_router.get(URL_HOME.home.reg.nonlin.poly, tags=['Calculate Regression'])
async def calculate_r_nonlinear_polynomial(x: str = Query(...), y: str = Query(...), n: int = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values, 'n': n}

    response = requests.post(URL_REQ.home.reg.nonlin.poly, json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')
