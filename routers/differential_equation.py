
from fastapi import Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
import requests

from models.const import URL_HOME, URL_REQ


differential_equation_router = APIRouter()

@differential_equation_router.get(URL_HOME.home.d_e.lin_approx, tags=['Differential Equations'])
async def calculate_de_lin_approx(x: str = Query(...), y: str = Query(...), func: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y, 'func_expr': func}

    response = requests.post(URL_REQ.home.d_e.lin_approx, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)
