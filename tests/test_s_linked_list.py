import pytest
from structures.s_linked_list import SingularlyLinkedList

@pytest.fixture
def sample_list():
    ll = SingularlyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    return ll

def test_add():
    ll = SingularlyLinkedList()
    ll.add(10)
    assert len(ll) == 1
    assert ll.get() == 10

def test_append(sample_list):
    assert len(sample_list) == 3
    sample_list.append(4)
    assert len(sample_list) == 4

def test_get(sample_list):
    assert sample_list.get() == 1
    assert len(sample_list) == 2

def test_get_empty():
    ll = SingularlyLinkedList()
    with pytest.raises(IndexError):
        ll.get()

def test_remove(sample_list):
    sample_list.remove(2)
    assert len(sample_list) == 2
    with pytest.raises(ValueError):
        sample_list.remove(42)

def test_is_empty():
    ll = SingularlyLinkedList()
    assert ll.isEmpty()
    ll.append(1)
    assert not ll.isEmpty()

def test_pop_end(sample_list):
    assert sample_list.pop() == 3
    assert len(sample_list) == 2

def test_pop_index(sample_list):
    assert sample_list.pop(1) == 2
    assert len(sample_list) == 2

def test_pop_index_out_of_bounds():
    ll = SingularlyLinkedList()
    ll.append(1)
    with pytest.raises(ValueError):
        ll.pop(2)

def test_set(sample_list):
    sample_list.set(1, 42)
    assert sample_list.pop(1) == 42

def test_set_index_out_of_bounds(sample_list):
    with pytest.raises(ValueError):
        sample_list.set(5, 100)

def test_insert_at_head():
    ll = SingularlyLinkedList()
    ll.append(1)
    ll.insert(0, 99)
    assert ll.pop(0) == 99

def test_insert_index_out_of_bounds():
    ll = SingularlyLinkedList()
    ll.append(1)
    with pytest.raises(IndexError):
        ll.insert(5, 10)

def test_str(sample_list):
    assert str(sample_list) == "[1, 2, 3]"

def test_str_empty():
    ll = SingularlyLinkedList()
    assert str(ll) == "[]"