# tests/test_main.py
from fastapi.testclient import TestClient
from weather_monitor.main import app

client = TestClient(app)


def test_read_weather():
    response = client.get("/api/weather/")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)

    # Response should be paginated to only return 10 elements
    assert len(response_json) == 10

    first_item = response_json[0]
    # First item should be dictionary with expected keys
    assert isinstance(first_item, dict)
    assert set(first_item.keys()) == {
        'id',
        'weather_station_name',
        'date',
        'precipitation',
        'max_temperature',
        'min_temperature'
    }

    # ensure results are floating point
    print(first_item)

def test_read_stats():
    response = client.get("/api/weather/stats")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)

    # Response should be paginated to only return 10 elements
    assert len(response_json) == 10

    first_item = response_json[0]
    # First item should be dictionary with expected keys
    assert isinstance(first_item, dict)
    assert set(first_item.keys()) == {
        'id',
        'weather_station_name',
        'year',
        'total_precipitation',
        'avg_max_temperature',
        'avg_min_temperature'
    }
    print(first_item)
