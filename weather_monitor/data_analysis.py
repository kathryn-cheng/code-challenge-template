from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, MetaData, Table, text
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from fastapi.responses import JSONResponse

from weather_monitor.database_engine import SessionLocal, engine


sql = """
INSERT INTO weather_data_analysis (year, weather_station_id, avg_min_temperature, avg_max_temperature, total_precipitation)
SELECT

    extract(year from "date") as year,
    weather_station_id,

    AVG(weather_data.min_temperature) as avg_min_temperature,
    AVG(weather_data.max_temperature) as avg_max_temperature,
    SUM(precipitation) as precipitation

FROM weather_data
group by
    weather_station_id,
    extract(year from "date")
"""

# FastAPI endpoint to calculate and return statistics
def calculate_statistics(db: Session):
   db.execute(text(sql))
   db.commit()

def run_analysis():
    with SessionLocal() as db:
        calculate_statistics(db)


if __name__ == "__main__":
    run_analysis()