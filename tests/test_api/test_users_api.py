import pytest
from httpx import AsyncClient
from app.main import app
from app.utils.nickname_gen import generate_nickname
from urllib.parse import urlencode

# Shared fixtures


@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest.fixture
def user_token():
    return "valid_user_token"


@pytest.fixture
def admin_token():
    return "valid_admin_token"


@pytest.fixture
def manager_token():
    return "valid_manager_token"


@pytest.mark.asyncio
async def test_create_user_access_denied(async_client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    user_data = {
        "nickname": generate_nickname(),
        "email": "test@example.com",
        "password": "StrongPassword123!",
    }
    response = await async_client.post("/users/", json=user_data, headers=headers)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_retrieve_user_access_denied(async_client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.get("/users/12345", headers=headers)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_retrieve_user_access_allowed(async_client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.get("/users/12345", headers=headers)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_user_email_access_denied(async_client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    updated_data = {"email": "updated_email@example.com"}
    response = await async_client.put("/users/12345", json=updated_data, headers=headers)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_update_user_email_access_allowed(async_client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    updated_data = {"email": "updated_email@example.com"}
    response = await async_client.put("/users/12345", json=updated_data, headers=headers)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_login_success(async_client):
    form_data = {
        "username": "valid_email@example.com",
        "password": "SecurePassword123!",
    }
    response = await async_client.post(
        "/login/",
        data=urlencode(form_data),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
