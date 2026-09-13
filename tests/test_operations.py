import pytest
from app.operations import addition,subtraction,multiplication,division
def test_addition_positive():
    assert addition(1,1)==2

def test_addition_negative():
    assert addition(1,-11)==-10

def test_subtraction_positive():
    assert subtraction(1,1)==0

def test_subtraction_negative():
    assert subtraction(-1,1)==-2
    assert subtraction(-1,-1)==0

def test_multiplication_positive():
    assert multiplication(16,16)==256

def test_multiplication_negative():
    assert multiplication(-16,16)==-256
    assert multiplication(16,-16)==-256
    assert multiplication(-16,-16)==256

def test_division_positive():
    assert division(256,16)==16

def test_division_negative():
    assert division(256,-16)==-16
    assert division(-256,16)==-16
    assert division(-256,-16)==16

def test_division_DivideByZero():
    with pytest.raises(ValueError, match="Can't Divide By Zero"):
        division(256,0)