class DenseGraph:
    """
    A graph implementation.
    Space complexity of O(n^2)
    """
    def __init__(self, node_count):
        """
        Initialize an empty dense graph with defined maximum number of nodes.
            Implementation is a matrix where a 1 in (i, j) represents an edge between nodes i and j
            and a 1 in (i,i) represents the presence of node i.

        :param node_count: The number of maximum nodes in the graph.
        """
        super().__init__()
        self.__nodes = [[0 for _ in range(0, i+1)] for i in range(node_count)]
        self.__node_count = node_count

    def add_node(self, value):
        """
        Add a node to the graph. O(1)

        :param value: The node to add.

        :raises KeyError: If the node is already present.
        :raises ValueError: If the node value is out of bounds.
        """
        if value < 0 or value >= self.__node_count:
            raise ValueError("Node value out of range.")
        if self.__nodes[value][value] == 1:
            raise KeyError("Node already present.")
        self.__nodes[value][value] = 1

    def add_edge(self, source, destination):
        """
        Add an edge between two nodes. O(1)

        :param source: First node of edge.
        :param destination: Second node of edge.

        :raises ValueError: If the same node is input twice.
        :raises ValueError: If either node value is out of bounds.
        :raises KeyError: If either node is not present.
        :raises KeyError: If the edge is already present.
        """
        min_node, max_node = min(source, destination), max(source, destination)
        if source == destination:
            raise ValueError("Cannot add an edge between same node.")
        if min_node < 0 or max_node >= self.__node_count:
            raise ValueError("Node value out of range.")
        if self.__nodes[source][source] == 0 or self.__nodes[destination][destination] == 0:
            raise KeyError("Node not found.")
        if self.isAdjacent(source, destination):
            raise KeyError("Edge already present.")
        self.__nodes[max_node][min_node] = 1

    def remove_node(self, value):
        """
        Remove a node from the graph. O(n)

        :param value: The node to be removed.

        :raises ValueError: If the node value is out of bounds.
        :raises KeyError: Raised if the node is not in the graph.
        """
        if value < 0 or value >= self.__node_count:
            raise ValueError("Node value out of range.")
        if self.__nodes[value][value] == 0:
            raise KeyError("Node not found.")
        self.__nodes[value] = [0 for _ in range(value+1)]
        for index in range(value+1, self.__node_count):
            self.__nodes[index][value] = 0

    def remove_edge(self, source, destination):
        """
        Remove an edge between two nodes. O(1)

        :param source: First node of edge.
        :param destination: Second node of edge.

        :raises ValueError: If the node value is out of bounds.
        :raises KeyError: Raised if either node is not in the graph.
        """
        min_node, max_node = min(source, destination), max(source, destination)
        if min_node < 0 or max_node >= self.__node_count:
            raise ValueError("Node value out of range.")
        if self.__nodes[min_node][min_node] == 0 or self.__nodes[max_node][max_node] == 0:
            raise KeyError("Node not found.")
        if source != destination:
            self.__nodes[max_node][min_node] = 0

    def get_connected_nodes(self, value):
        """
        Return a list of nodes connected to a node. O(n)

        :param value: The source node to get connected nodes from.

        :return: A list of nodes connected to a node.

        :raises ValueError: If the node value is out of bounds.
        :raises KeyError: Raised if the node is not in the graph.
        """
        if value < 0 or value >= self.__node_count:
            raise ValueError("Node value out of range.")
        if self.__nodes[value][value] == 0:
            raise KeyError("Node not found.")
        nodes = []
        for index in range(self.__node_count):
            if self.isAdjacent(value, index):
                nodes.append(index)
        return nodes

    def get_nodes(self):
        """
        Return list of nodes. O(n)

        :return: List of nodes present.
        """
        nodes = []
        for index in range(self.__node_count):
            if self.__nodes[index][index] == 1:
                nodes.append(index)
        return nodes

    def isAdjacent(self, source, destination):
        """
        Return True if the two nodes share an edge. O(1)

        :param source: First node of edge.
        :param destination: Second node of edge.

        :return: True if the two nodes share an edge, False otherwise.

        :raises ValueError: If the node value is out of bounds.
        """
        min_node, max_node = min(source, destination), max(source, destination)
        if min_node < 0 or max_node >= self.__node_count:
            raise ValueError("Node value out of range.")
        return self.__nodes[max_node][min_node] == 1 and source != destination

    def isPresent(self, node):
        """
        Return True if the node is present. O(n)

        :param node: The node to check.

        :return: True if the node is present, False otherwise.

        :raises ValueError: If the node value is out of bounds.
        """
        if node < 0 or node >= self.__node_count:
            raise ValueError("Node value out of range.")
        return self.__nodes[node][node] == 1