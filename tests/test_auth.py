# test_auth.py
# Unit tests for auth.py

import os
import json
import pytest
from src.js_tap_tap import auth


@pytest.fixture
def mock_users_db(tmp_path, monkeypatch):
    """Fixture to isolate the tests from the real users.json file."""
    db_path = tmp_path / "test_users.json"
    monkeypatch.setattr(auth, "USER_DB", str(db_path))
    return str(db_path)


def test_load_users_creates_empty_db(mock_users_db):
    """Test that loading users creates an empty JSON if the file doesn't exist."""
    assert not os.path.exists(mock_users_db)
    users = auth.load_users()
    assert users == {}
    assert os.path.exists(mock_users_db)
    with open(mock_users_db, "r") as f:
        assert json.load(f) == {}


def test_hash_password():
    """Test the password hashing logic."""
    salt = "1234567890abcdef"
    password = "my_secret_password"
    hashed = auth.hash_password(password, salt)
    assert isinstance(hashed, str)
    assert len(hashed) == 64  # SHA-256 hex digest length
    
    # Ensure same input produces same output
    assert auth.hash_password(password, salt) == hashed
    # Ensure different password produces different output
    assert auth.hash_password("different_password", salt) != hashed
    # Ensure different salt produces different output
    assert auth.hash_password(password, "fedcba0987654321") != hashed


def test_create_and_verify_user(mock_users_db):
    """Test full registration and login flow."""
    username = "test_user"
    password = "test_password"
    
    # 1. Registration
    ok, msg = auth.create_user(username, password)
    assert ok is True
    assert msg == "Registered."
    
    users = auth.load_users()
    assert username in users
    assert "salt" in users[username]
    assert "hash" in users[username]
    assert users[username]["highscore"] == 0
    
    # 2. Duplicate registration should fail
    ok, msg = auth.create_user(username, "another_password")
    assert ok is False
    assert msg == "Username already exists."
    
    # 3. Successful login
    ok, msg = auth.verify_user(username, password)
    assert ok is True
    assert msg == "Login successful."
    
    # 4. Incorrect password
    ok, msg = auth.verify_user(username, "wrong_password")
    assert ok is False
    assert msg == "Incorrect password."
    
    # 5. Non-existent user
    ok, msg = auth.verify_user("non_existent_user", "password")
    assert ok is False
    assert msg == "Account not found."


def test_highscore_persistence(mock_users_db):
    """Test highscore updating and retrieval."""
    username = "score_test_user"
    auth.create_user(username, "password123")
    
    # Initial score should be 0
    assert auth.get_highscore(username) == 0
    
    # Update to 10
    auth.update_highscore(username, 10)
    assert auth.get_highscore(username) == 10
    
    # Lower score should not overwrite
    auth.update_highscore(username, 5)
    assert auth.get_highscore(username) == 10
    
    # Higher score should overwrite
    auth.update_highscore(username, 50)
    assert auth.get_highscore(username) == 50
