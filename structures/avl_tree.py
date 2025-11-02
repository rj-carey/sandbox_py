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

    def __get_height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.__get_height() + 1
        elif self.right is None:
            return self.left.__get_height() + 1
        else:
            return max(self.left.__get_height(), self.right.__get_height()) + 1

    def update_bf(self):
        hr = 0 if self.right is None else self.right.__get_height()
        hl = 0 if self.left is None else self.left.__get_height()
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
            self.__root = y
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
            self.__root = y
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

        # Check and update rotated root
        parent = self.root.parent
        while parent is not None:
            self.root = parent
            parent = self.root.parent

    def add_node(self, value):
        """
        Add a node to the tree, ensuring AVL condition is retained. O(log n)

        :param value: The data to add.

        :raises ValueError: If the node is already present.
        """
        if not self.__root:
            self.root = AVLNode(value)
            return
        current = self.__root
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

    def remove_node(self, value):
        """
        Remove a node from the tree, ensuring AVL condition is retained.

        :param value: The data to remove.

        :raises ValueError: If the node is not present.
        """
        if self.__root is None:
            raise ValueError("Node does not exist.")
        else:
            current_node = self.__root
            path = []
            while current_node is not None:
                path.append(current_node)
                if current_node.value < value:
                    current_node = current_node.right
                elif current_node.value > value:
                    current_node = current_node.left
                else:
                    #replace node
                    #update bfs
                    #rebalance
                    pass
            raise ValueError("Node does not exists.")