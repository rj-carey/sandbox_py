class Node:
    """
    A node in a singly linked list.
    """
    def __init__(self, data):
        """Initialize an empty node."""
        self.data = data # Stores the data at this node
        self.next = None # Stores the reference to the next element

class SingularlyLinkedList:
    """
    A singularly linked list implementation similar.
    Space complexity of O(n).
    """

    def __init__(self):
        """Initialize an empty singularly linked list."""
        self.__head = None # Stores the reference to the first element in the list

    def add(self, data):
        """
        Pre-pend an element to the start of the array. O(1)

        :param data: The data to append.
        """
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node

    def append(self, data):
        """
        Append an element to the end of the array. O(n)

        :param data: The data to append.
        """
        if self.isEmpty():
            self.add(data)
        else:
            new_node = Node(data)
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node

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

    def remove(self, data):
        """
        Remove the first occurrence of a value. O(n)

        :param data: The value to remove.

        :raises ValueError: If value is not in the array.
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


    def pop(self, index=-1):
        """
        Remove and return element at index (default last). O(n)

        :param index: Index of the element to pop.
        :return: The removed element.

        :raises IndexError: If index is out of bounds.
        """
        if index == -1:
            index = len(self.__head)-1
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

    def get(self):
        """
        Retrieve the first element of the singularly linked list. O(1)

        :return: The data of the first element.

        :raises IndexError: If list is empty.
        """
        if self.isEmpty():
            raise IndexError("The linked list is empty.")
        data = self.__head.data
        self.__head = self.__head.next
        return data

    def set(self, index, data):
        """
        Set the data at a specific index. O(n)

        :param index: The index to update.
        :param data: The new data.

        :raises IndexError: If index is out of bounds.
        """
        if index < 0 or index >= len(self):
            raise ValueError("Index out of bounds.")
        counter = 0
        current = self.__head
        while counter < index:
            current = current.next
        current.data = data

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