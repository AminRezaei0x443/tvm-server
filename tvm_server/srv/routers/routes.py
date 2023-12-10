from fastapi.routing import APIRouter

from .models import GetMethodRequest


router = APIRouter()


@router.post("/tvm/get-method")
async def run_get_method(rq: GetMethodRequest):
    return {}


@router.get("/")
async def root():
    return {"message": "Welcome To The TVM Server"}
