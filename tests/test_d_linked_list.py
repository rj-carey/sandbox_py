import pytest
from structures.d_linked_list import DoublyLinkedList

@pytest.fixture
def empty_list():
    return DoublyLinkedList()

@pytest.fixture
def populated_list():
    dll = DoublyLinkedList()
    for i in range(5):
        dll.add(i)
    return dll

def test_add_single_element(empty_list):
    empty_list.add(10)
    assert str(empty_list) == "[10]"

def test_add_multiple_elements(empty_list):
    empty_list.add(1)
    empty_list.add(2)
    empty_list.add(3)
    assert str(empty_list) == "[1, 2, 3]"

def test_insert_at_head(empty_list):
    empty_list.add(10)
    empty_list.insert(0, 5)
    assert str(empty_list) == "[5, 10]"

def test_insert_at_middle(populated_list):
    populated_list.insert(2, 99)
    assert populated_list.peek(2) == 99

def test_insert_at_tail(populated_list):
    length = len(populated_list)
    populated_list.insert(length - 1, 999)
    assert populated_list.peek(length - 1) == 999

def test_insert_out_of_bounds(empty_list):
    with pytest.raises(IndexError):
        empty_list.insert(2, 5)

def test_get_head(populated_list):
    first = populated_list.peek(0)
    got = populated_list.get(0)
    assert got == first
    assert len(populated_list) == 4

def test_get_tail(populated_list):
    last = populated_list.peek(-1)
    got = populated_list.get(-1)
    assert got == last
    assert len(populated_list) == 4

def test_get_middle(populated_list):
    val = populated_list.peek(2)
    got = populated_list.get(2)
    assert got == val
    assert len(populated_list) == 4

def test_get_out_of_bounds(populated_list):
    with pytest.raises(IndexError):
        populated_list.get(10)

def test_remove_head(populated_list):
    val = populated_list.peek(0)
    populated_list.remove(val)
    assert populated_list.peek(0) != val

def test_remove_tail(populated_list):
    val = populated_list.peek(-1)
    populated_list.remove(val)
    assert str(populated_list) == "[0, 1, 2, 3]"

def test_remove_middle(populated_list):
    val = populated_list.peek(2)
    populated_list.remove(val)
    assert str(populated_list) == "[0, 1, 3, 4]"

def test_remove_not_found(populated_list):
    with pytest.raises(ValueError):
        populated_list.remove(999)

def test_remove_from_empty(empty_list):
    with pytest.raises(IndexError):
        empty_list.remove(1)

def test_set_value(populated_list):
    populated_list.set(2, 999)
    assert populated_list.peek(2) == 999

def test_set_invalid_index(populated_list):
    with pytest.raises(ValueError):
        populated_list.set(10, 1)

def test_peek_value(populated_list):
    assert populated_list.peek(2) == 2

def test_peek_negative_index(populated_list):
    assert populated_list.peek(-1) == 4

def test_peek_invalid_index(populated_list):
    with pytest.raises(ValueError):
        populated_list.peek(100)

def test_is_empty_true(empty_list):
    assert empty_list.isEmpty()

def test_is_empty_false(populated_list):
    assert not populated_list.isEmpty()

def test_len_empty(empty_list):
    assert len(empty_list) == 0

def test_len_non_empty(populated_list):
    assert len(populated_list) == 5

def test_str_empty(empty_list):
    assert str(empty_list) == "[]"

def test_str_populated(populated_list):
    assert str(populated_list) == "[0, 1, 2, 3, 4]"

def test_repr(populated_list):
    assert repr(populated_list) == str(populated_list)
