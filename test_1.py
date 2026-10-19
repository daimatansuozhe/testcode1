import pandas as pd
import pytest

data1=pd.read_csv('correct_case.csv', dtype=str)
data1.fillna('')

list1_data1=data1.values.tolist()

print(list1_data1)

@pytest.fixture(autouse=True)
def user():
    userinfo={"username":"abc","password":"123"}
    yield userinfo
@pytest.mark.parametrize(
    "username,password",list1_data1
)
def test_1(user,username,password):
    assert user["username"]==username
    assert user["password"]==password


#wrong case
data_wrong=pd.read_csv('wrong_case.csv')
data_wrong.fillna('')
list_data_wrong=data_wrong.values.tolist()

@pytest.mark.parametrize(
    'wrong_username,wrong_password',list_data_wrong
)

@pytest.mark.xfail()
def test_name_empty(user,wrong_username,wrong_password):
    assert user["username"]==wrong_username
    assert user["password"]==wrong_password
    assert len(wrong_password)<10
    assert not any(char in wrong_password for char in '!@#%^$&')


