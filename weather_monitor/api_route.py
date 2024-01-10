from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import joinedload

from weather_monitor.deps import SessionDep
from weather_monitor.models import WeatherData, WeatherDataAnalysis
from weather_monitor.schemas import WeatherDataSchema, WeatherDataAnalysisSchema

router = APIRouter()


@router.get(
    "/weather/",
    response_model=List[WeatherDataSchema],
    response_description="Weather Data Items",
)
def read_weather_entries(db: SessionDep, skip: int = 0, limit: int = 10):
    entries = (
        db.query(WeatherData)
        .options(joinedload(WeatherData.weather_station))
        .order_by(WeatherData.id)
        .offset(skip)
        .limit(limit)
        .all()
    )

    response = [
        WeatherDataSchema(
            id=entry.id,
            weather_station_name=entry.weather_station.station_name,
            date=str(entry.date),
            min_temperature=entry.min_temperature,
            max_temperature=entry.max_temperature,
            precipitation=entry.precipitation,
        )
        for entry in entries
    ]
    return response


@router.get(
    "/weather/stats",
    response_model=List[WeatherDataAnalysisSchema],
    response_description="Weather Data Analysis Items",
)
def read_weather_analysis(
    db: SessionDep,
    skip: int = 0,
    limit: int = 10,
):
    entries = (
        db.query(WeatherDataAnalysis)
        .options(joinedload(WeatherDataAnalysis.weather_station))
        .order_by(WeatherDataAnalysis.id)
        .offset(skip)
        .limit(limit)
        .all()
    )

    response = [
        WeatherDataAnalysisSchema(
            id=entry.id,
            year=str(entry.year),
            weather_station_name=entry.weather_station.station_name,
            avg_min_temperature=entry.avg_min_temperature,
            avg_max_temperature=entry.avg_max_temperature,
            total_precipitation=entry.total_precipitation,
        )
        for entry in entries
    ]
    return response
