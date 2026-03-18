import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Signup
    resp_signup = client.post(f"/activities/{activity}/signup?email={email}")
    assert resp_signup.status_code == 200 or resp_signup.status_code == 400
    # Unregister
    resp_unreg = client.delete(f"/activities/{activity}/unregister?email={email}")
    assert resp_unreg.status_code == 200 or resp_unreg.status_code == 404
