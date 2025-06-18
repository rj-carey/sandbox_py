class BTNode:
    """
    A node in a binary tree.
    """
    def __init__(self, value):
        """Initialize an empty node."""
        self.value = value  # The data of the node
        self.parent = None  # Pointer to the parent node
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child

    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value

class BinaryTree:
    """
    A binary tree data structure.
    Class constants for traversal mode.
    Space complexity: O(n)
    """
    PREORDER = 0
    INORDER = 1
    POSTORDER = 2
    LEVELORDER = 3

    def __init__(self):
        """Initialize an empty tree."""
        self.__root = None

    def add_node(self, value):
        """
        Add a node to the tree. O(n) [but average case O(log n)]

        :param value: The data of the node.

        :raises ValueError: If the node is already present.
        """
        new_node = BTNode(value)
        if self.__root is None:
            self.__root = new_node
        else:
            current_node = self.__root
            while current_node is not None:
                if new_node.value == current_node.value:
                    raise ValueError("Node already exists.")
                if new_node < current_node:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        new_node.parent = current_node
                        return
                elif new_node > current_node:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        new_node.parent = current_node
                        return

    @staticmethod
    def __find_replacement(node):
        """
        Static method to find the rightmost node of the left subtree of a node.

        :param node: The node for which to find a replacement

        :return: The replacement node.
        """
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        node = node.left
        while node.right:
            node = node.right
        return node

    def remove_node(self, value):
        """
        Remove a node from the tree. O(n) [but average case O(log n)]

        :param value: The data of the node to be removed.

        :raises ValueError: If the tree is empty.
        :raises ValueError: If the node does not exist.
        """
        if self.__root is None:
            raise ValueError("The tree is empty.")
        if self.__root.value == value:
            replacement = self.__find_replacement(self.__root)
            if replacement:
                replacement.parent.right = replacement.left
                replacement.left = self.__root.left
                replacement.right = self.__root.right
            self.__root = replacement
        else:
            current_node = self.__root
            while current_node is not None:
                if value < current_node.value:
                    if current_node.left:
                        if current_node.left.value == value:
                            replacement = self.__find_replacement(current_node.left)
                            if replacement:
                                replacement.parent.right = replacement.left
                                replacement.left = current_node.left.left
                                replacement.right = current_node.left.right
                            current_node.left = replacement
                        else:
                            current_node = current_node.left
                    else:
                        raise ValueError("Node does not exist.")
                elif value > current_node.value:
                    if current_node.right:
                        if current_node.right.value == value:
                            replacement = self.__find_replacement(current_node.right)
                            if replacement:
                                replacement.parent.right = replacement.left
                                replacement.left = current_node.right.left
                                replacement.right = current_node.right.right
                            current_node.right = replacement
                        else:
                            current_node = current_node.right
                    else:
                        raise ValueError("Node does not exist.")

    def find_node(self, value):
        """
        Find a node in the tree. O(n) [but average case O(log n)]

        :param value: The data of the node to be found.

        :return: The node or None if it does not exist.
        """
        current_node = self.__root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value == current_node.value:
                return current_node
            else:
                current_node = current_node.right
        return None

    def __preorder(self, node):
        """Preorder traversal of the tree."""
        if node is None:
            return
        print(f"{node.value}, ", end="")
        self.__preorder(node.left)
        self.__preorder(node.right)

    def __inorder(self, node):
        """Inorder traversal of the tree."""
        if node is None:
            return
        self.__inorder(node.left)
        print(f"{node.value}, ", end="")
        self.__inorder(node.right)

    def __postorder(self, node):
        """Postorder traversal of the tree."""
        if node is None:
            return
        self.__postorder(node.left)
        self.__postorder(node.right)
        print(f"{node.value}, ", end="")

    def __levelorder(self, node):
        """Level-order traversal of the tree."""
        to_handle = [node]
        while to_handle:
            node = to_handle.pop(0)
            if node:
                to_handle += [node.left, node.right]
                print(f"{node.value}, ", end="")

    def traverse(self, mode):
        """
        Traverse the tree, print the value of each node in the specified order. O(n)

        :param mode: Traversal method in [0,1,2,3]

        :return:
        """
        if not mode in [0,1,2,3]:
            raise ValueError("Invalid mode.")
        if mode == 0:
            self.__preorder(self.__root)
        elif mode == 1:
            self.__inorder(self.__root)
        elif mode == 2:
            self.__postorder(self.__root)
        elif mode == 3:
            self.__levelorder(self.__root)

    def __height(self, node):
        """Helper method to return the height of the tree."""
        if node is None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1

    def get_height(self):
        """Return the height of the tree."""
        return self.__height(self.__root)

    def get_size(self):
        """Return the number of nodes in the tree."""
        nodes = [self.__root]
        count = 0
        while nodes:
            node = nodes.pop(0)
            if node:
                count += 1
                nodes += [node.left, node.right]
