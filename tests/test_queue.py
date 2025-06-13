import pytest
from structures.queue import Queue

def test_add_and_peek():
    s = Queue()
    s.add(1)
    s.add(2)
    assert s.peek() == 1  # First added is on top
    assert not s.isEmpty()

def test_get():
    s = Queue()
    s.add('x')
    s.add('y')
    assert s.get() == 'x'
    assert s.get() == 'y'
    assert s.isEmpty()

def test_get_empty_raises():
    s = Queue()
    with pytest.raises(IndexError, match="Queue is empty."):
        s.get()

def test_peek_empty_raises():
    s = Queue()
    with pytest.raises(IndexError, match="Queue is empty."):
        s.peek()

def test_is_empty_true_and_false():
    s = Queue()
    assert s.isEmpty()
    s.add(10)
    assert not s.isEmpty()

def test_str_and_repr():
    s = Queue()
    s.add(1)
    s.add(2)
    s.add(3)
    expected = "[1, 2, 3, ...]"
    assert s.__str__() == expected
    assert repr(s) == expected