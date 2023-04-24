import pytest


@pytest.fixture()
def set_up():
    print("Enter in system")
    yield
    print("Exit from system")

@pytest.fixture(scope="module")
def scope():
    print("Enter")
    yield
    print("Exit")