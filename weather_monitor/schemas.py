
import pydantic

class WeatherDataSchema(pydantic.BaseModel):
    min_temperature: float
    max_temperature: float
    precipitation: float


class WeatherDataAnalysisSchema(pydantic.BaseModel):
    avg_min_temperature: float
    avg_max_temperature: float
    total_precipitation: float
