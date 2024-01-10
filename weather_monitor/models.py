from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from weather_monitor.database_engine import Base


# Data Model
class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True)
    date = Column(Date, index=True)
    weather_station_id = Column(
        Integer, ForeignKey("weather_station.id"), nullable=False
    )
    max_temperature = Column(Float)
    min_temperature = Column(Float)
    precipitation = Column(Float)


class WeatherDataAnalysis(Base):
    __tablename__ = "weather_data_analysis"

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    weather_station_id = Column(
        Integer, ForeignKey("weather_station.id"), nullable=False
    )
    avg_max_temperature = Column(Float, nullable=True)
    avg_min_temperature = Column(Float, nullable=True)
    total_precipitation = Column(Float, nullable=True)


class WeatherStation(Base):
    __tablename__ = "weather_station"

    id = Column(Integer, primary_key=True, autoincrement=True)
    station_name = Column(String, index=True)

    weather_data_items = relationship(WeatherData, backref="weather_station")
    weather_data_analysis_items = relationship(
        WeatherDataAnalysis, backref="weather_station"
    )


if __name__ == "__main__":
    print("Give to alembic", Base.metadata.tables)
