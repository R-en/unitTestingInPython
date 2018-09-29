import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSet up session")


@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSet up module")\


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSet up function")


def test1():
    print("Executing test 1")
    assert True


def test2():
    print("Executing test 2")
    assert True