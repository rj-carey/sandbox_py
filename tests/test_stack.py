import pytest
from structures.stack import Stack

def test_add_and_peek():
    s = Stack()
    s.add(1)
    s.add(2)
    assert s.peek() == 2  # Last added is on top
    assert not s.isEmpty()

def test_get():
    s = Stack()
    s.add('x')
    s.add('y')
    assert s.get() == 'y'
    assert s.get() == 'x'
    assert s.isEmpty()

def test_get_empty_raises():
    s = Stack()
    with pytest.raises(IndexError, match="Stack is empty."):
        s.get()

def test_peek_empty_raises():
    s = Stack()
    with pytest.raises(IndexError, match="Stack is empty."):
        s.peek()

def test_is_empty_true_and_false():
    s = Stack()
    assert s.isEmpty()
    s.add(10)
    assert not s.isEmpty()

def test_str_and_repr():
    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)
    expected = "[1, 2, 3, ...]"
    assert s.__str__() == expected
    assert repr(s) == expected
