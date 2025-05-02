class DataStore:
    """
    A base class for data structures.
    """

    @staticmethod
    def add(data):
        """
        Add an element to the structure, the position it is added to depends on the structure type.

        :param data: The data to add.
        """
        return "add() not implemented for this structure type."

    @staticmethod
    def insert(index, data):
        """
        Insert an element at a specified index.

        :param index: Index at which to insert.
        :param data: The data to insert.

        :raises IndexError: If index is out of bounds.
        """
        return "insert() not implemented for this structure type."

    @staticmethod
    def get(index):
        """
        Get and delete the element at a specific index.

        :param index: The index to retrieve.
        :return: The data at the index.

        :raises IndexError: If index is out of bounds.
        """
        return "get() not implemented for this structure type."

    @staticmethod
    def remove(data):
        """
        Remove the first occurrence of an element.

        :param data: The data to remove.

        :raises ValueError: If value is not in the array.
        :raises IndexError: If list is empty.
        """
        return "remove() not implemented for this structure type."

    @staticmethod
    def set(index, data):
        """
        Set an element at a specific index.

        :param index: The index to update.
        :param data: The new data.

        :raises IndexError: If index is out of bounds.
        """
        return "set() not implemented for this structure type."

    @staticmethod
    def peek(index):
        """
        Return the element at a specific index.

        :param index: The index to retrieve.
        :return: The data at the index.

        :raises IndexError: If index is out of bounds.
        """
        return "peek() not implemented for this structure type."
