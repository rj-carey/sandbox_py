import pytest
from structures.s_linked_list import SingularlyLinkedList

@pytest.fixture
def linked_list():
    ll = SingularlyLinkedList()
    ll.add(3)
    ll.add(2)
    ll.add(1)
    return ll  # List is now [1, 2, 3]

def test_add():
    ll = SingularlyLinkedList()
    ll.add(10)
    assert str(ll) == "[10]"

def test_insert_start():
    ll = SingularlyLinkedList()
    ll.add(2)
    ll.insert(0, 1)
    assert str(ll) == "[1, 2]"

def test_insert_middle(linked_list):
    linked_list.insert(1, 99)
    assert str(linked_list) == "[1, 99, 2, 3]"

def test_insert_end(linked_list):
    linked_list.insert(3, 100)
    assert str(linked_list) == "[1, 2, 3, 100]"

def test_inset_negative_index(linked_list):
    linked_list.insert(-2, 99)
    assert str(linked_list) == "[1, 2, 99, 3]"

def test_insert_invalid():
    ll = SingularlyLinkedList()
    with pytest.raises(IndexError):
        ll.insert(5, 10)

def test_get_start(linked_list):
    value = linked_list.get(0)
    assert value == 1
    assert str(linked_list) == "[2, 3]"

def test_get_end(linked_list):
    value = linked_list.get(-1)
    assert value == 3
    assert str(linked_list) == "[1, 2]"

def test_get_invalid_index():
    ll = SingularlyLinkedList()
    with pytest.raises(ValueError):
        ll.get(0)

def test_remove_head():
    ll = SingularlyLinkedList()
    ll.add(1)
    ll.add(2)
    ll.remove(2)
    assert str(ll) == "[1]"

def test_remove_middle(linked_list):
    linked_list.remove(2)
    assert str(linked_list) == "[1, 3]"

def test_remove_nonexistent():
    ll = SingularlyLinkedList()
    ll.add(1)
    with pytest.raises(ValueError):
        ll.remove(10)

def test_remove_nonexistent_long():
    ll = SingularlyLinkedList()
    ll.add(3)
    ll.add(2)
    ll.add(1)
    with pytest.raises(ValueError):
        ll.remove(10)

def test_remove_from_empty():
    ll = SingularlyLinkedList()
    with pytest.raises(IndexError):
        ll.remove(1)

def test_set_middle(linked_list):
    linked_list.set(1, 42)
    assert str(linked_list) == "[1, 42, 3]"

def test_set_negative_index(linked_list):
    linked_list.set(-1, 99)
    assert str(linked_list) == "[1, 2, 99]"

def test_set_invalid_index():
    ll = SingularlyLinkedList()
    with pytest.raises(ValueError):
        ll.set(0, 1)

def test_peek_start(linked_list):
    assert linked_list.peek(0) == 1

def test_peek_middle(linked_list):
    assert linked_list.peek(1) == 2

def test_peek_end(linked_list):
    assert linked_list.peek(2) == 3

def test_peek_negative_index(linked_list):
    assert linked_list.peek(-1) == 3
    assert linked_list.peek(-2) == 2

def test_peek_invalid_index_positive(linked_list):
    with pytest.raises(ValueError):
        linked_list.peek(5)

def test_peek_invalid_index_negative(linked_list):
    with pytest.raises(ValueError):
        linked_list.peek(-4)

def test_peek_on_empty():
    ll = SingularlyLinkedList()
    with pytest.raises(ValueError):
        ll.peek(0)

def test_is_empty():
    ll = SingularlyLinkedList()
    assert ll.isEmpty()
    ll.add(1)
    assert not ll.isEmpty()

def test_len(linked_list):
    assert len(linked_list) == 3

def test_str(linked_list):
    assert str(linked_list) == "[1, 2, 3]"

def test_empty_str():
    ll = SingularlyLinkedList()
    assert str(ll) == "[]"

def test_repr(linked_list):
    assert repr(linked_list) == "[1, 2, 3]"
