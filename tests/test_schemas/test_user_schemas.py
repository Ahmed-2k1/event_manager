import pytest
from datetime import datetime
from pydantic import ValidationError
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, LoginRequest

# Reusable fixture data


@pytest.fixture
def user_base_data():
    return {
        "nickname": "valid_nickname",
        "email": "valid_email@example.com",
        "profile_picture_url": "http://valid.com/profile.jpg",
    }


@pytest.fixture
def user_create_data():
    return {
        "nickname": "valid_nickname",
        "email": "valid_email@example.com",
        "password": "SecurePassword123!",
    }


@pytest.fixture
def user_update_data():
    return {
        "email": "updated_email@example.com",
        "profile_picture_url": "http://updated.com/profile.jpg",
    }


@pytest.fixture
def user_response_data():
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",  # Valid UUID
        "email": "user_response@example.com",
        "created_at": datetime.now(),
        "last_login_at": datetime.now(),
    }


@pytest.fixture
def login_request_data():
    return {
        "email": "valid_email@example.com",
        "password": "SecurePassword123!",
    }

# Test cases


def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]


def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]


def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]


def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert str(user.id) == user_response_data["id"]


def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]


@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname


@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)


@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url


@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)
