import pytest


@pytest.fixture()
def set_up():
    print("Start test run")
    yield
    print("Finish test run")

@pytest.fixture(scope="module")
def set_group():
    print("Enter into the system")

    yield
    print("Exit system")
