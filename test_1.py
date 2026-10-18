import pytest

@pytest.fixture()
def user():
    username={"username":"user","password":"123"}
    yield username
@pytest.mark.parametrize("username,password", [("user","123"), ("user","1234")])
def test_user(user,username, password):
    assert username == user['username'] and password == user['password']