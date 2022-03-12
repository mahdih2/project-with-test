from cods.main import sum_of_number, sub_of_number, prod_of_number
import pytest

@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 7, 11)])
def test_sum(a, b, c):
    assert sum_of_number(a, b) == c

def test_sub():
    assert sub_of_number(5, 2) == 3

def test_prod():
    assert prod_of_number(2, 8) == 16