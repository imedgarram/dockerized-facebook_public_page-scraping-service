from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main_api():
    response = client.post("/reuters")
    assert response.status_code == 200
