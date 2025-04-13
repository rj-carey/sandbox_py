class Array:
    """
    A simple dynamic array implementation similar to Python's built-in list.
    """

    def __init__(self):
        """Initialize an empty array."""
        self._data = []

    def append(self, value):
        """
        Append an element to the end of the array.

        :param value: The value to append.
        """
        self._data.append(value)

    def insert(self, index, value):
        """
        Insert a value at a specified index.

        :param index: Index at which to insert.
        :param value: The value to insert.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0 or index > len(self._data):
            raise IndexError("Index out of bounds.")
        self._data.insert(index, value)

    def remove(self, value):
        """
        Remove the first occurrence of a value.

        :param value: The value to remove.

        :raises ValueError: If value is not in the array.
        """
        self._data.remove(value)

    def pop(self, index=-1):
        """
        Remove and return element at index (default last).

        :param index: Index of the element to pop.
        :return: The removed element.

        :raises IndexError: If index is out of bounds.
        """
        return self._data.pop(index)

    def get(self, index):
        """
        Get the value at a specific index.

        :param index: The index to retrieve.
        :return: The value at the index.

        :raises IndexError: If index is out of bounds.
        """
        return self._data[index]

    def set(self, index, value):
        """
        Set a value at a specific index.

        :param index: The index to update.
        :param value: The new value.

        :raises IndexError: If index is out of bounds.
        """
        self._data[index] = value

    def size(self):
        """
        Get the number of elements in the array.

        :return: int: The size of the array.
        """
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)
