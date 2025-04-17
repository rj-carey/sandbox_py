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
        self.prev = None # Stores the reference to the previous element

class DoublyLinkedList(DataStore):
    """
    A doubly linked list implementation.
    Space complexity of O(n).
    """
    def __init__(self):
        """Initialize an empty doubly linked list."""
        super().__init__()
        self.__head = None # Stores the reference to the first element in the list
        self.__tail = None # Stores the reference to the last element in the list

    @override
    def add(self, data):
        """
        Append an element to the doubly linked list. O(1)

        :param data: The data to append.
        """
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

    @override
    def insert(self, index, data):
        """
        Insert an element at a specified index. O(n)

        :param index: Index at which to insert.
        :param data: The data to insert.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0:
            index += len(self) + 1
        if index < 0 or index > len(self):
            raise IndexError("Index out of bounds.")
        if index == len(self):
            self.add(data)
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        else:
            new_node = Node(data)
            counter = 1
            current = self.__head.next
            while counter < index:
                current = current.next
                counter += 1
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

    @override
    def get(self, index=-1):
        """
        Get and delete the element at a specific index. O(n)

        :param index: The index to retrieve.
        :return: The data at the index.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0:
            index += len(self) + 1
        if index < 0 or index > len(self):
            raise IndexError("Index out of bounds.")
        if index == 0:
            target = self.__head
            self.__head = target.next
            if self.__head is None:
                self.__tail = None
            else:
                self.__head.prev = None
            return target.data
        elif index == len(self)-1:
            target = self.__tail
            self.__tail = target.prev
            self.__tail.next = None
            return target.data
        else:
            counter = 1
            current = self.__head.next
            while counter < index:
                current = current.next
                counter += 1
            current.prev.next = current.next
            current.next.prev = current.prev
            return current.data

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
        if self.__head.data == data:
            self.__head = self.__head.next
            if self.__head is None:
                self.__tail = None
            else:
                self.__head.prev = None
        elif self.__tail.data == data:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            current = self.__head.next
            if current is None:
                raise ValueError("Value not found.")
            while current.data != data:
                current = current.next
                if current is None:
                    raise ValueError("Value not found.")
            current.prev.next = current.next
            current.next.prev = current.prev

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
    def peek(self, index):
        """
        Return the element at a specific index. O(n)

        :param index: The index to retrieve.
        :return: The data at the index.

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
        return current.data

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