import pytest
from structures.priority_queue import PriorityQueue

def test_add_and_peek():
    s = PriorityQueue()
    s.add(1)
    s.add(2)
    assert s.peek() == 1  # First added is on top
    assert not s.isEmpty()

def test_get():
    s = PriorityQueue()
    s.add(1)
    s.add(2)
    assert s.get() == 1
    assert s.get() == 2
    assert s.isEmpty()

def test_get_empty_raises():
    s = PriorityQueue()
    with pytest.raises(IndexError, match="Queue is empty."):
        s.get()

def test_peek_empty_raises():
    s = PriorityQueue()
    with pytest.raises(IndexError, match="Queue is empty."):
        s.peek()

def test_is_empty_true_and_false():
    s = PriorityQueue()
    assert s.isEmpty()
    s.add(10)
    assert not s.isEmpty()

def test_str_and_repr():
    s = PriorityQueue()
    s.add(1)
    s.add(2)
    s.add(3)
    expected = "[1, 2, 3, ...]"
    assert s.__str__() == expected
    assert repr(s) == expected

def test_priority():
    s = PriorityQueue()
    s.add(3)
    s.add(4)
    s.add(0)
    s.add(1)
    s.add(5)
    s.add(2)
    s.add(3)
    s.add(3)
    assert s.__str__() == "[0, 1, 2, 3, 3, 3, 4, 5, ...]"