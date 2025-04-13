import pytest
from structures.array import Array

def test_append():
    arr = Array()
    arr.append(10)
    arr.append(20)
    assert arr.size() == 2
    assert arr.get(0) == 10
    assert arr.get(1) == 20

def test_insert():
    arr = Array()
    arr.append(1)
    arr.append(3)
    arr.insert(1, 2)
    assert arr.get(1) == 2

def test_remove():
    arr = Array()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.remove(2)
    assert arr.size() == 2
    with pytest.raises(ValueError):
        arr.remove(4)

def test_pop():
    arr = Array()
    arr.append(5)
    arr.append(6)
    value = arr.pop()
    assert value == 6
    assert arr.size() == 1

def test_get_set():
    arr = Array()
    arr.append(0)
    arr.set(0, 99)
    assert arr.get(0) == 99

def test_index_errors():
    arr = Array()
    with pytest.raises(IndexError):
        arr.insert(1, 100)
    with pytest.raises(IndexError):
        arr.get(0)
    with pytest.raises(IndexError):
        arr.set(0, 10)
    with pytest.raises(IndexError):
        arr.pop()
