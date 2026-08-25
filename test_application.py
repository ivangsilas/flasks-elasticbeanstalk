import pytest
from application import application

@pytest.fixture
def client():
    application.config["TESTING"] = True
    with application.test_client() as client:
        yield client

def test_home_loads(client):
    response = client.get("/")
    assert response.status_code == 200

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.get_json()

def test_add_note(client):
    response = client.post("/add", data={"note": "Buy milk"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy milk" in response.data