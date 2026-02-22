from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={"message": "What is the capital of India?"})
    assert response.status_code == 200
    assert "response" in response.json()