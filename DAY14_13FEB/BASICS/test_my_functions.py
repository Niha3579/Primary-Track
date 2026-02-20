import pytest
import my_functions as my_functions

assert my_functions.add(5,7)==10

def test_add():
    assert my_functions.add(2,3)==5
    assert my_functions.add(5,7)==10


def test_str_add():
    assert my_functions.add("I like ","cricket")=="I like cricket"


def test_divide():
    with pytest.raises(ValueError):
        my_functions.divide(20,0)

    with pytest.raises(ZeroDivisionError):
        my_functions.divide(100,0)

    assert my_functions.divide(100,0)==10   