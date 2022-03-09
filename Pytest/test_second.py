import pytest


def test_addition():
    a = 10
    assert a == 30


@pytest.mark.skip
def test_creditcard1():
    print("credit card")


@pytest.mark.smoke
def test_password():
    print("Enter the password")