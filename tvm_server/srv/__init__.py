from app.routers import router
from app.core.data_manager import DataManager
from fastapi import FastAPI

DataManager.init("server.db")
app = FastAPI()
app.include_router(router)
