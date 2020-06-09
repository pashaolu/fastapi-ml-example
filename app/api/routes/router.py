from fastapi import APIRouter
from app.api.routes import index,heartbeat,prediction


api = APIRouter()
api.include_router(index.router, tags=["index"])
api.include_router(heartbeat.router, tags=["health"])
api.include_router(prediction.router, tags=["prediction"])