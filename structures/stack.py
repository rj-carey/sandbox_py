from structures.data_store import DataStore
from typing import override

class Stack(DataStore):
    """
    A stack implementation.
    Space complexity of O(n).
    """
    def __init__(self):
        """Initialize an empty stack."""
        self.__store = []

    @override
    def add(self, data):
        """
        Add an element to the top of the stack. O(1)

        :param data: The data to add.
        """
        self.__store.insert(0, data)

    @override
    def get(self):
        """
        Get and delete the element on the top of the stack. O(1)

        :return: The data at the index.

        :raises IndexError: If stack is empty.
        """
        if self.isEmpty:
            raise IndexError("Stack is empty.")
        return self.__store.pop(0)

    @override
    def peek(self):
        """
        Return the element on the top of the stack. O(1).

        :return: The data at the index.

        :raises IndexError: If stack is empty.
        """
        if self.isEmpty:
            raise IndexError("Stack is empty.")
        return self.__store[0]

    def isEmpty(self):
        """
        Return True if the stack is empty, False otherwise. O(1)

        :return bool: True if the list is empty, False otherwise.
        """
        return self.__store == []

    def __str__(self):
        return ["..."] + self.__store

    def __repr__(self):
        return self.__str__()