from app import add

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0