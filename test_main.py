from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_meal_names():
    response = client.get("http://127.0.0.1:8000/menu/2021-03-03/MEAL_KIT")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == ["Tomato-braised chicken with sweet potato and chard",
                               "Miso-ginger ground pork and summer squash donburi",
                               "Mediterranean braise with zucchini, new potatoes, and capers",
                               "Catalan chicken with green romesco and Spanish green beans",
                               "Chipotle chilaquiles with black beans and fried eggs",
                               "Moroccan chicken with carrots, snap peas, and spicy green harissa"]


def test_bad_date():
    response = client.get("http://127.0.0.1:8000/menu/20210303/MEAL_KIT")
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == {"detail": "Invalid date format"}


def test_bad_meal_type():
    response = client.get("http://127.0.0.1:8000/menu/2021-03-03/MEALKIT")
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == {"detail": "Invalid meal type"}


def test_no_meals_available():
    response = client.get("http://127.0.0.1:8000/menu/2021-01-01/MEAL_KIT")
    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == {"detail": "No meals found"}
