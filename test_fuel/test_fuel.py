from fuel import convert
from fuel import gauge
import pytest
def main():
    test_in()
    test_zero()
    test_v()

def test_in():
    assert convert("3/4")== 75 and gauge(75)== "75%"
    assert convert("1/2")== 50 and gauge(50)== "50%"
    assert convert("1/4")== 25 and gauge(25)== "25%"
    assert convert("4/4")== 100 and gauge(100)== "F"
    assert convert("99/100")== 99 and gauge(99)== "F"
    assert convert("1/100")== 1 and gauge(1)== "E"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_v():
    with pytest.raises(ValueError):
        convert("three/four")
        convert("1.5/3")








