import pytest

def test_demo0(setup):
    print("This is demo 0 ")


@pytest.fixture
def demo1():
    print("This is fixture demo1")
    yield
    print("I will be executed after the test case is done")


def test_demo2(demo1):
    print("this is demo 2")