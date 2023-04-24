import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print("Method 1")

@pytest.mark.run(order=2)
def test_method_2():
    print("Method 2")

@pytest.mark.run(order=6)
def test_method_3():
    print("Method 3")
@pytest.mark.run(order=4)
def test_method_4():
    print("Method 4")
@pytest.mark.run(order=3)
def test_method_5():
    print("Method 5")
@pytest.mark.run(order=5)
def test_method_6():
    print("Method 6")