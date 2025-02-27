import jwt
import pytest

from app import schemas
from app.config import settings


def test_create_user(client):
    response = client.post(
        "/users", json={"email": "test@gmail.com", "password": "password123"}
    )
    new_user = schemas.User(**response.json())
    assert new_user.email == "test@gmail.com"
    assert response.status_code == 201


def test_login_user(test_user, client):
    response = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    login_token = schemas.Token(**response.json())
    payload = jwt.decode(
        login_token.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_token.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@gmail.com", "password123", 403),
        ("test@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "password123", 403),
        ("test@gmail.com", None, 403)
    ],
)
def test_incorrect_login(test_user, client, email, password, status_code):
    response = client.post(
        "/login", data={"username": email, "password": password}
    )
    assert response.status_code == status_code
