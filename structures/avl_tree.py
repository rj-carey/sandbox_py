class AVLNode:
    """
    A node in an AVL tree
    """
    def __init__(self, value, parent=None):
        """Initialize the node"""
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.balance_factor = 0

    def get_height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.get_height() + 1
        elif self.right is None:
            return self.left.get_height() + 1
        else:
            return max(self.left.get_height(), self.right.get_height()) + 1

    def update_bf(self):
        hr = 0 if self.right is None else self.right.get_height()
        hl = 0 if self.left is None else self.left.get_height()
        self.balance_factor = hr-hl

class AVLTree:
    """
    An AVL tree is a self-balancing binary search tree invented by Adelson-Velsky and Landis.
    Balance factor of a node is the height of the right subtree minus the height of the left subtree.
    AVL condition: All nodes have a balance factor in {-1, 0, 1}.
    Thus, the height is always O(log n)
    """
    def __init__(self):
        self.root = None

    def __rotate_left(self, z):
        """
        Perform a left rotation on node z.
        """
        y = z.right
        z.right = y.left
        if y.left:
            y.left.parent = z

        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y

        y.left = z
        z.parent = y

        # Update balance factors
        z.update_bf()
        y.update_bf()

    def __rotate_right(self, z):
        """
        Perform a right rotation on node z.
        """
        y = z.left
        z.left = y.right
        if y.right:
            y.right.parent = z

        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y

        y.right = z
        z.parent = y

        # Update balance factors
        z.update_bf()
        y.update_bf()

    def __rebalance(self, node):
        """
        Rebalance the subtree rooted at 'node' and update parents/root.
        """
        # Left heavy
        if node.balance_factor < -1:
            # Check for Left-Right case
            if node.left and node.left.balance_factor > 0:
                self.__rotate_left(node.left)
            self.__rotate_right(node)
        # Right heavy
        elif node.balance_factor > 1:
            # Check for Right-Left case
            if node.right and node.right.balance_factor < 0:
                self.__rotate_right(node.right)
            self.__rotate_left(node)

    def add_node(self, value):
        """
        Add a node to the tree, ensuring AVL condition is retained. O(log n)

        :param value: The data to add.

        :raises ValueError: If the node is already present.
        """
        if not self.root:
            self.root = AVLNode(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = AVLNode(value, parent=current)
                    break
            elif value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = AVLNode(value, parent=current)
                    break
            else:
                raise ValueError("Node already exists.")
        while current:
            current.update_bf()
            if abs(current.balance_factor) > 1:
                self.__rebalance(current)
                break
            current = current.parent

    def __transplant(self, u, v):
        """Helper method: replace subtree rooted at u with subtree rooted at v."""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def remove_node(self, value):
        """
        Remove a node from the tree, ensuring AVL condition is retained.

        :param value: The data to remove.

        :raises ValueError: If the node is not present.
        """
        node = self.root
        while node and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        if node is None:
            raise ValueError("Node does not exist.")

        if node.left is None and node.right is None:
            # Case 1: no children
            parent = node.parent
            self.__transplant(node, None)
        elif node.left is None:
            # Case 2: only right child
            parent = node.parent
            self.__transplant(node, node.right)
        elif node.right is None:
            # Case 3: only left child
            parent = node.parent
            self.__transplant(node, node.left)
        else:
            # Case 4: two children → find in-order successor
            successor = node.right
            while successor.left:
                successor = successor.left
            parent = successor.parent
            if successor.parent != node:
                self.__transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.__transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

        while parent:
            parent.update_bf()
            if abs(parent.balance_factor) > 1:
                self.__rebalance(parent)
            parent = parent.parent

    def find_node(self, value):
        """
        Find a node in the tree. O(log n)

        :param value: The data to find.

        :return: True if node is present, False otherwise.
        """
        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False