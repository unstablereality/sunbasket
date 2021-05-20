from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_meal_names():
    pass


def test_bad_date():
    pass


def test_bad_meal_type():
    pass
