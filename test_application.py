from application import application
import pytest

@pytest.fixture
def client():
    application.config["TESTING"] = True
    with application.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_greet(client):
    response = client.get("/greet/Chuka")
    assert response.get_json() == {"message": "Hello, Chuka!"}