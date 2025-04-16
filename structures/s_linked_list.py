from structures.data_store import DataStore
from typing import override

class Node:
    """
    A node in a singly linked list.
    """
    def __init__(self, data):
        """Initialize an empty node."""
        self.data = data # Stores the data at this node
        self.next = None # Stores the reference to the next element

class SingularlyLinkedList(DataStore):
    """
    A singularly linked list implementation similar.
    Space complexity of O(n).
    """
    def __init__(self):
        """Initialize an empty singularly linked list."""
        super().__init__()
        self.__head = None # Stores the reference to the first element in the list

    @override
    def add(self, data):
        """
        Pre-pend an element to the start of the list. O(1)

        :param data: The data to append.
        """
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node

    @override
    def insert(self, index, data):
        """
        Insert an element at the given index in the list. O(n)

        :param index: Index at which to insert.
        :param data: The data to insert.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of bounds.")
        if index == 0:
            self.add(data)
        else:
            new_node = Node(data)
            counter = 1
            current = self.__head
            while counter < index:
                current = current.next
                counter += 1
            new_node.next = current.next
            current.next = new_node

    @override
    def get(self, index=0):
        """
        Get and delete the element at a specific index. O(n)

        :param index: The index to retrieve.
        :return: The data at the index.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise ValueError("Index out of bounds.")
        if index == 0:
            current = self.__head
            self.__head = current.next
            return current.data
        else:
            counter = 1
            current = self.__head
            while counter < index:
                current = current.next
                counter += 1
            target = current.next
            current.next = target.next
            return target.data

    @override
    def remove(self, data):
        """
        Remove the first occurrence of an element. O(n)

        :param data: The data to remove.

        :raises ValueError: If value is not in the array.
        :raises IndexError: If list is empty.
        """
        if self.isEmpty():
            raise IndexError("List is empty.")
        current = self.__head
        if current.data == data:
            self.__head = current.next
        elif current.next is None:
            raise ValueError("Value not found.")
        else:
            while current.next.data != data:
                current = current.next
                if current.next is None:
                    raise ValueError("Value not found.")
            current.next = current.next.next

    @override
    def set(self, index, data):
        """
        Set an element at a specific index. O(n)

        :param index: The index to update.
        :param data: The new data.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise ValueError("Index out of bounds.")
        counter = 0
        current = self.__head
        while counter < index:
            current = current.next
            counter += 1
        current.data = data

    @override
    def peek(self, index=0):
        """
        Return the element at a specific index.

        :param index: The index to retrieve.
        :return: The data at the index.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise ValueError("Index out of bounds.")
        if index == 0:
            return self.__head.data
        else:
            counter = 1
            current = self.__head
            while counter < index:
                current = current.next
                counter += 1
            return current.next.data

    def isEmpty(self):
        """
        Return True if the list is empty, False otherwise. O(1)

        :return bool: True if the list is empty, False otherwise.
        """
        return self.__head is None

    def __len__(self):
        """
        Return the length of the list. O(n)

        :return int: Length of the list.
        """
        counter = 0
        current = self.__head
        while current:
            counter += 1
            current = current.next
        return counter

    def __str__(self):
        if self.isEmpty():
            return "[]"
        out_str = "["
        current = self.__head
        while current:
            out_str += str(current.data) + ", "
            current = current.next
        return out_str[:-2] + "]"

    def __repr__(self):
        return self.__str__()
