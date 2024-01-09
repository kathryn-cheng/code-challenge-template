from fastapi import Depends, FastAPI, HTTPException
from weather_monitor.api_route import router

app = FastAPI()

app.include_router(router, prefix="/api")
