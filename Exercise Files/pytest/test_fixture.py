import pytest

@pytest.fixture()
def setup1():
    print("\nSet up 1")
    yield
    print("\nTear down 1")

@pytest.fixture()
def setup2(request):
    print("Set up 2")

    def teardown_a():
        print("Tear Down a")

    def teardown_b():
        print("\nTear down b")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test 1")
    assert True


def test2(setup2):
    print("Executing test 2")
    assert True