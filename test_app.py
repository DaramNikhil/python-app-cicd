from app import add, substract

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_substract():
    assert substract(5, 1) == 2
    assert substract(5 - 5) == 0