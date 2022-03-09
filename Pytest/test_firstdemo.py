# This is the first pytest demo program
import pytest


def test_helloworld():
    print("Hello, Welcome to pytest")


def test_visacard():
    print("This is for visa card")


def test_debitcard():
   print("this is for debit card")


def test_add1():
    a = 5
    b = 6
    print(a+b)


@pytest.mark.smoke
def test_login():
    print("Enter the login ID")
