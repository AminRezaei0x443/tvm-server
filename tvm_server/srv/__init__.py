from tvm_server.srv.routers import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
