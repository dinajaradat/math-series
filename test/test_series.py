import pytest
from series import fibonacci
from series import lucas
from series import sum_series


def test_0():
    actual=fibonacci(0)
    expected=0
    assert actual == expected

def test_one():
    actual=fibonacci(1)
    expected=1
    assert actual == expected

def test_two():
    actual=fibonacci(4)
    expected=3
    assert actual == expected

def test2_0():
    actual=lucas(0)
    expected=2
    assert actual == expected

def test2_one():
    actual=lucas(1)
    expected=1
    assert actual == expected

def test2_two():
    actual=lucas(2)
    expected=3
    assert actual == expected

def test2_three():
    actual=lucas(3)
    expected=4
    assert actual == expected

def test3_one():
    actual=sum_series(3,3,1)
    expected=2
    assert actual == expected

def test3_two():
    actual=sum_series(3)
    expected=2
    assert actual == expected

