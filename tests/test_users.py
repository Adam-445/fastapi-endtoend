from app import schemas
from .database import client, session


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to my API!"}


def test_create_user(client):
    response = client.post(
        "/users", json={"email": "test@gmail.com", "password": "password123"}
    )
    print(response.json())
    new_user = schemas.User(**response.json())
    assert new_user.email == "test@gmail.com"
    assert response.status_code == 201


def test_login_user(client):
    response = client.post(
        "/login", data={"username": "test@gmail.com", "password": "password123"}
    )
    print(response.json())
    assert response.status_code == 200
