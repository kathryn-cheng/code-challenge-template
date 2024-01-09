from typing import Annotated

import pydantic
from fastapi import Body


class WeatherDataSchema(pydantic.BaseModel):
    id: int
    weather_station_name: str
    date: str
    min_temperature: Annotated[float, Body(description="Average minimum temperature in degrees Celsius")]
    max_temperature: Annotated[float, Body(description="Average maximum temperature in degrees Celsius")]
    precipitation: Annotated[float, Body(description="Average minimum temperature in centimeters")]


class WeatherDataAnalysisSchema(pydantic.BaseModel):
    id: int
    year: int
    weather_station_name: str
    avg_min_temperature: Annotated[float, Body(description="Average minimum temperature in degrees Celsius")]
    avg_max_temperature: Annotated[float, Body(description="Average maximum temperature in degrees Celsius")]
    total_precipitation: Annotated[float, Body(description="Average minimum temperature in centimeters")]
