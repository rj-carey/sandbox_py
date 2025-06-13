from structures.data_store import DataStore
from typing import override

class Queue(DataStore):
    """
    A queue implementation.
    Space complexity of O(n).
    """
    def __init__(self):
        """Initialize an empty queue."""
        self.__store = []

    @override
    def add(self, data):
        """
        Add an element to the back of the queue. O(1)

        :param data: The data to add.
        """
        self.__store.append(data)

    @override
    def get(self):
        """
        Get and delete the element at the front of the queue. O(n)

        :return: The data at the index.

        :raises IndexError: If queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Queue is empty.")
        return self.__store.pop(0)

    @override
    def peek(self):
        """
        Return the element at the front of the queue. O(1).

        :return: The data at the index.

        :raises IndexError: If queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Queue is empty.")
        return self.__store[0]

    def isEmpty(self):
        """
        Return True if the stack is empty, False otherwise. O(1)

        :return bool: True if the list is empty, False otherwise.
        """
        return self.__store == []

    def __str__(self):
        return f"{str(self.__store)[:-1]}, ...]"

    def __repr__(self):
        return self.__str__()