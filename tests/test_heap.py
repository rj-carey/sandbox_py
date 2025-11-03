import pytest
from structures.heap import Heap, MinHeap, MaxHeap


def test_min_heap_push_and_pop_order():
    heap = MinHeap()
    values = [5, 3, 8, 1, 2]
    for v in values:
        heap.push(v)

    # Popping should give sorted order for a min-heap
    popped = [heap.pop() for _ in range(len(values))]
    assert popped == sorted(values)
    assert heap.isEmpty()
    assert heap.size() == 0


def test_max_heap_push_and_pop_order():
    heap = MaxHeap()
    values = [5, 3, 8, 1, 2]
    for v in values:
        heap.push(v)

    # Popping should give reverse-sorted order for a max-heap
    popped = [heap.pop() for _ in range(len(values))]
    assert popped == sorted(values, reverse=True)
    assert heap.isEmpty()


def test_pop_empty_raises_value_error():
    heap = Heap()
    with pytest.raises(ValueError):
        heap.pop()


def test_peek_and_size_behavior():
    heap = MinHeap()
    for v in [10, 4, 7]:
        heap.push(v)
    assert heap.peek() == 4
    assert heap.size() == 3
    heap.pop()
    assert heap.peek() in [7, 10]
    assert heap.size() == 2


def test_is_empty_flags_correctly():
    heap = Heap()
    assert heap.isEmpty()
    heap.push(42)
    assert not heap.isEmpty()
    heap.pop()
    assert heap.isEmpty()


def test_sift_up_multiple_swaps():
    # Insert descending numbers to trigger repeated sifts up
    heap = MinHeap()
    for v in range(10, 0, -1):
        heap.push(v)
    assert heap.peek() == 1
    assert heap.size() == 10


def test_heap_restores_order_after_pop_min():
    heap = MinHeap()
    for v in [10, 20, 5, 15, 25]:
        heap.push(v)

    popped = heap.pop()
    assert popped == 5  # smallest
    # next root should be smallest of remaining
    assert heap.peek() == 10


def test_heap_restores_order_after_pop_max():
    heap = MaxHeap()
    for v in [10, 20, 5, 15, 25]:
        heap.push(v)

    popped = heap.pop()
    assert popped == 25  # largest
    # next root should be next largest
    assert heap.peek() in [20, 15]


def test_heap_with_one_child_cases():
    """Covers internal branches for single-child scenarios."""
    # Case: only left child
    heap = MinHeap()
    heap.data = [10, 5]  # simulate direct setup
    heap.push(7)         # triggers sift up/down and child check
    assert heap.peek() == 5

    # Case: only right child
    heap = MinHeap()
    heap.data = [10]
    heap.push(15)
    assert heap.peek() == 10


def test_heap_compare_and_parent_logic():
    """Covers __compare and __get_parent indirectly via normal use."""
    min_heap = MinHeap()
    max_heap = MaxHeap()

    # For min heap, smaller value bubbles up
    min_heap.push(2)
    min_heap.push(1)
    assert min_heap.peek() == 1

    # For max heap, larger value bubbles up
    max_heap.push(1)
    max_heap.push(2)
    assert max_heap.peek() == 2

    # __get_parent indirectly covered through recursive push() structure
    assert not min_heap.isEmpty()
    assert not max_heap.isEmpty()


def test_heap_with_complex_structure_and_multiple_pops():
    heap = MinHeap()
    for v in [50, 30, 40, 10, 20, 35, 45]:
        heap.push(v)

    popped_sequence = [heap.pop() for _ in range(len(heap.data))]
    assert popped_sequence == sorted(popped_sequence)


def test_pop_until_empty():
    heap = MaxHeap()
    for v in [3, 1, 2]:
        heap.push(v)
    assert not heap.isEmpty()
    while not heap.isEmpty():
        heap.pop()
    assert heap.isEmpty()
