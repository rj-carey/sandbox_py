class Array:
    """
    A simple dynamic array implementation similar to Python's built-in list.
    """

    def __init__(self):
        """Initialize an empty array."""
        self.__data = []

    def append(self, data):
        """
        Append an element to the end of the array.

        :param data: The value to append.
        """
        self.__data.append(data)

    def insert(self, index, data):
        """
        Insert a value at a specified index.

        :param index: Index at which to insert.
        :param data: The value to insert.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0 or index > len(self.__data):
            raise IndexError("Index out of bounds.")
        self.__data.insert(index, data)

    def remove(self, data):
        """
        Remove the first occurrence of a value.

        :param data: The value to remove.

        :raises ValueError: If value is not in the array.
        """
        self.__data.remove(data)

    def pop(self, index=-1):
        """
        Remove and return element at index (default last).

        :param index: Index of the element to pop.
        :return: The removed element.

        :raises IndexError: If index is out of bounds.
        """
        return self.__data.pop(index)

    def get(self, index):
        """
        Get the value at a specific index.

        :param index: The index to retrieve.
        :return: The value at the index.

        :raises IndexError: If index is out of bounds.
        """
        return self.__data[index]

    def set(self, index, data):
        """
        Set a value at a specific index.

        :param index: The index to update.
        :param data: The new value.

        :raises IndexError: If index is out of bounds.
        """
        self.__data[index] = data

    def size(self):
        """
        Get the number of elements in the array.

        :return int: The size of the array.
        """
        return len(self.__data)

    def __str__(self):
        return str(self.__data)

    def __len__(self):
        return len(self.__data)
