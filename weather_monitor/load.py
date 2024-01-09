import pandas as pd
from glob import glob

from sqlalchemy import Column, Integer
from sqlalchemy.testing import db

from weather_monitor.database_engine import SessionLocal
from weather_monitor.models import WeatherData, WeatherStation

import re


def is_valid_value(val):
    return val != 9999 and val != -9999 and val != 999


def extract_station_code(file_path):
    # Define the regular expression pattern with an optional directory name
    pattern = r'(?:.*/)?(\w+)\.txt'

    # Use re.search to find the pattern in the file_path
    match = re.search(pattern, file_path)

    # If a match is found, return the extracted station code, else return None
    return match.group(1) if match else None


def load_weather_data(filename, db):
    df = pd.read_fwf(
        filename,
        header=None,
        names=['date', 'max_temperature', 'min_temperature', 'precipitation']
    )
    # Insert data into the database

    df['date'] = df['date'].astype(str)
    print(df)

    station_name = extract_station_code(filename)
    weather_station = db.query(WeatherStation).filter(WeatherStation.station_name == station_name).first()
    if weather_station is None:
        weather_station = WeatherStation(station_name=station_name)
        db.add(weather_station)
        db.flush()

    weather_station_id = weather_station.id

    print(filename)

    for _, row in df.iterrows():
        weather_data = WeatherData(
            date=row["date"],
            max_temperature=row["max_temperature"] if is_valid_value(row["max_temperature"]) else None,
            min_temperature=row["min_temperature"] if is_valid_value(row["min_temperature"]) else None,
            precipitation=row["precipitation"] if is_valid_value(row["precipitation"]) else None,
            weather_station_id=weather_station_id
        )
        db.add(weather_data)

    db.commit()


def load_all_weather_files():
    with SessionLocal() as db:
        for filename in glob("wx_data/*.txt"):
            load_weather_data(filename, db)



if __name__ == "__main__":
    load_all_weather_files()
