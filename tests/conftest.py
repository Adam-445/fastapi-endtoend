import pytest
from fastapi.testclient import TestClient

from app.database import get_db, Base
from app.main import app
from .database import TestSessionLocal, engine
from app.oauth2 import create_access_token
from app import models


@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(session):
    # run our code before we run the test
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    # runs this code after the test finishes


@pytest.fixture
def test_user(client):
    user_data = {"email": "test@gmail.com", "password": "password123"}
    response = client.post("/users", json=user_data)

    assert response.status_code == 201
    user_all_data = response.json()
    user_all_data["password"] = user_data["password"]
    return user_all_data

@pytest.fixture
def test_user2(client):
    user_data = {"email": "test2@gmail.com", "password": "password"}
    response = client.post("/users", json=user_data)

    assert response.status_code == 201
    user_all_data = response.json()
    user_all_data["password"] = user_data["password"]
    return user_all_data


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}
    return client

@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user['id']
    }, {
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user['id']
    },
        {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user['id']
    }, {
        "title": "4th title",
        "content": "4th content",
        "owner_id": test_user2['id']
    }]
    session.add_all([models.Post(**post) for post in posts_data])
    session.commit()
    return session.query(models.Post).all()