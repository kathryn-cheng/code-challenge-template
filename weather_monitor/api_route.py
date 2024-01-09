from typing import List

from fastapi import APIRouter, HTTPException
from weather_monitor.deps import SessionDep
from weather_monitor.models import WeatherData, WeatherDataAnalysis
from weather_monitor.schemas import WeatherDataSchema, WeatherDataAnalysisSchema

router = APIRouter()


@router.get(
    "/weather/",
    response_model=List[WeatherDataSchema],
    response_description="Weather Data Items"
)
def read_weather_entries(db: SessionDep, skip: int = 0, limit: int = 10):
    entries = db.query(WeatherData).order_by(WeatherData.id).offset(skip).limit(limit).all()
    return entries



@router.get(
    "/weather/stats",
    response_model=List[WeatherDataAnalysisSchema],
    response_description="Weather Data Analysis Items"
)
def read_weather_analysis(db: SessionDep, skip: int = 0, limit: int = 10, ):
    entries = db.query(WeatherDataAnalysis).order_by(WeatherDataAnalysis.id).offset(skip).limit(limit).all()
    return entries
