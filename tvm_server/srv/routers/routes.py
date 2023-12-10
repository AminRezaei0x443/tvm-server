from fastapi.routing import APIRouter

from .models import GetMethodRequest
from tonpy.types import Cell
from tvm_server.tvm import run_get_method


router = APIRouter()


@router.post("/tvm/get-method")
async def tvm_get_method(rq: GetMethodRequest):
    code = Cell(rq.code)
    data = Cell(rq.data)
    if rq.config is not None and rq.config != "":
        config = Cell(rq.config)
    else:
        config = None

    method = rq.method
    if method == "":
        return {"error": "invalid method name"}

    g = run_get_method(code, data, method, config=config)
    return g.to_json()


@router.get("/")
async def root():
    return {"message": "Welcome To The TVM Server"}
