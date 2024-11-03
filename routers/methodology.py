from fastapi import APIRouter
from fastapi import Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests

from models.const import URL_HOME, URL_REQ


methodology_router = APIRouter()

@methodology_router.get(URL_HOME.home.meth.gauss, tags=['Methodology'])
async def calculate_m_gauss(a: int, b: int, n: int, func: str = Query(...)):

    playload = {'a': a, 'b': b, 'n': n, 'func_expr': func}

    response = requests.post(URL_REQ.home.meth.gauss, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)

@methodology_router.get(URL_HOME.home.meth.boole, tags=['Methodology'])
async def calculate_m_boole(a: int, b: int, n: int, func: str = Query(...)):

    playload = {'a': a, 'b': b, 'n': n, 'func_expr': func}

    response = requests.post(URL_REQ.home.meth.boole, json=playload)

    result = response.json()
    if response.status_code == 200:
        return JSONResponse(content=jsonable_encoder(result))
    else:
        return JSONResponse(content=jsonable_encoder(result), status_code=404)
