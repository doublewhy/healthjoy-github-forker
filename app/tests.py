import pytest
from fastapi.testclient import TestClient
from app.main import app, GITHUB_TOKEN, REPO_TO_FORK
from .forker import fork_repo

client = TestClient(app)


def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "Fork a GitHub Repository" in response.text


def test_fork_github_repo_success():
    # Test the app by forking the repo
    # Double check that you don't have a repo in your account before running the test
    payload = {
        "repo_name": REPO_TO_FORK,
        "token": GITHUB_TOKEN,
    }
    response = client.post("/", data=payload)
    assert response.status_code == 200
    assert "Fork Successful" in response.text


def test_fork_github_repo_exists():
    # Test the app by forking the already forked repo
    payload = {
        "repo_name": REPO_TO_FORK,
        "token": GITHUB_TOKEN,
    }
    response = client.post("/", data=payload)
    assert response.status_code == 500
    assert "Repository has already been forked" in response.text


def test_forker_empty_token():
    # Test the function by passing in an empty token
    with pytest.raises(Exception) as e:
        fork_repo(REPO_TO_FORK, "")
    assert str(e.value) == "GitHub access token cannot be empty"


def test_forker_empty_repo():
    # Test the function by passing in an empty repo
    with pytest.raises(Exception) as e:
        fork_repo("", GITHUB_TOKEN)
    assert str(e.value) == "Repo name cannot be empty"


def test_forker_invalid_token():
    # Test the function by passing in an invalid token
    invalid_token = "fjdskhfkdsh"
    with pytest.raises(Exception) as e:
        fork_repo(REPO_TO_FORK, invalid_token)
    assert "Bad credentials" in str(e.value)


def test_forker_invalid_repo():
    # Test the function by passing in an invalid repo
    invalid_repo = "fjdskhfkdsh"
    with pytest.raises(Exception) as e:
        fork_repo(invalid_repo, GITHUB_TOKEN)
    assert "Not Found" in str(e.value)
