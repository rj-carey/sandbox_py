class Heap:
    """
    Generalised array-based heap implementation for min- and max-heaps.
    """
    def __init__(self, is_min=True):
        """
        Initialise the empty heap, storing a flag defining if the heap is a min- or max-heap.
        Array-based, so root is index 0, left and right child of node at index n are index 2n+1 and 2n+2 respectively.

        :param is_min: Signifies if the heap is a min- or max-heap.
        """
        self.data = []
        self.is_min = is_min

    def __compare(self, a, b):
        """
        Compare two heap elements with the suitable comparison operator. O(1)

        :param a: The first element to compare.
        :param b: The second element to compare.

        :return: e.g. True if element a is smaller than element b, and it is a min-heap.
        """
        return a < b if self.is_min else a > b

    def __swap(self, a, b):
        """
        Swap the two nodes at the same time. O(1)

        :param a: the index of the first node to swap.
        :param b: the index of the second node to swap.
        """
        c = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = c

    @staticmethod
    def __get_parent(index):
        """
        Compute the parent of node at the input index. O(1)

        :param index: the index of the child.

        :return integer|None: the index of the parent node or None if no parent.
        """
        if index == 0:
            return None
        return (index-1) // 2

    def __get_children(self, index):
        """
        Compute the children indexes. O(1)

        :param index: the index of the parent.

        :return integer|None, integer|None: index of the children or None if no child in that direction.
        """
        left, right = (index*2)+1, (index*2)+2
        if left >= len(self.data):
            return None, None
        elif right >= len(self.data):
            return left, None
        else:
            return left, right

    def push(self, value):
        """
        Insert an element and restore heap property. O(log n)

        :param value: Data to insert.
        """
        self.data.append(value)
        self.__sift_up(len(self.data) - 1)

    def pop(self):
        """
        Remove and return root element. O(log n)

        :return element: the maximal/minimal element.
        """
        if not self.data:
            raise ValueError("Heap is empty")
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        root = self.data.pop()
        self.__sift_down(0)
        return root

    def __sift_up(self, child):
        """
        Sift an element up the heap until the heap condition is satisfied. O(log n)

        :param child: element index to sift.
        """
        parent = self.__get_parent(child)
        if parent is not None and self.__compare(self.data[child], self.data[parent]):
            self.__swap(child, parent)
            self.__sift_up(parent)

    def __sift_down(self, parent):
        """
        Sift an element down the heap until the heap condition is satisfied. O(log n)

        :param parent: element index to sift.
        """
        child_l, child_r = self.__get_children(parent)
        if not (child_l or child_r):
            return
        elif not child_l and self.__compare(self.data[child_r], self.data[parent]):
            self.__swap(parent, child_r)
            self.__sift_down(child_r)
        elif not child_r and self.__compare(self.data[child_l], self.data[parent]):
            self.__swap(parent, child_l)
            self.__sift_down(child_l)
        elif child_l and child_r:
            child = child_l if self.__compare(self.data[child_l], self.data[child_r]) else child_r
            if self.__compare(self.data[child], self.data[parent]):
                self.__swap(parent, child)
                self.__sift_down(child)

    def size(self):
        """
        Return the size of the heap, i.e., the number of elements in the heap. O(1)

        :return integer: the size of the heap.
        """
        return len(self.data)

    def isEmpty(self):
        """
        Check if the heap is empty. O(1)

        :return: True if heap is empty, False otherwise.
        """
        return self.size() == 0

    def peek(self):
        """
        Return the smallest/largest element in the heap. O(1)

        :return element: The smallest/largest element in the heap.
        """
        return self.data[0]


class MinHeap(Heap):
    def __init__(self):
        """
        Initialise the super class.
        """
        super().__init__(is_min=True)

class MaxHeap(Heap):
    def __init__(self):
        """
        Initialise the super class.
        """
        super().__init__(is_min=False)

if __name__ == '__main__':
    """Covers internal branches for single-child scenarios."""
    # Case: only left child
    heap = MinHeap()
    heap.data = [7, 10]  # simulate direct setup
    heap.push(5)         # triggers sift up/down and child check
    assert heap.peek() == 5

    # Case: only right child
    heap = MinHeap()
    heap.data = [10]
    heap.push(15)
    assert heap.peek() == 10