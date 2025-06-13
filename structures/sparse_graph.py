class SparseGraph:
    """
    A graph implementation.
    Space complexity of O(n^2)
    """
    def __init__(self):
        """Initialize an empty sparse graph."""
        super().__init__()
        self.__nodes = {} # Dictionary linking a node's ID to its adjacency list

    def add_node(self, value):
        """
        Add a node to the graph. O(1)

        :param value: The node to add.

        :raises KeyError: If the node is already present.
        """
        if value in self.__nodes.keys():
            raise KeyError("Node already present.")
        self.__nodes[value] = []

    def add_edge(self, source, destination):
        """
        Add an edge between two nodes. O(1)

        :param source: First node of edge.
        :param destination: Second node of edge.

        :raises KeyError: If the edge is already present.
        """
        if self.isAdjacent(source, destination):
            raise KeyError("Edge already present.")
        self.__nodes[source].append(destination)
        self.__nodes[destination].append(source)

    def remove_node(self, value):
        """
        Remove a node from the graph. O(n)

        :param value: The node to be removed.

        :raises KeyError: Raised if the node is not in the graph.
        """
        if value in self.__nodes.keys():
            neighbours = self.__nodes[value]
            for neighbour in neighbours:
                self.remove_edge(value, neighbour)
            self.__nodes.pop(value)
        else:
            raise KeyError("Node not found.")

    def remove_edge(self, source, destination):
        """
        Remove an edge between two nodes. O(n)

        :param source: First node of edge.
        :param destination: Second node of edge.

        :raises KeyError: Raised if either node is not in the graph.
        """
        if source in self.__nodes.keys() and destination in self.__nodes.keys():
            if destination in self.__nodes[source]:
                self.__nodes[source].remove(destination)
            if source in self.__nodes[destination]:
                self.__nodes[destination].remove(source)
        else:
            raise KeyError("Node not found.")

    def get_connected_nodes(self, value):
        """
        Return a list of nodes connected to a node. O(n)

        :param value: The source node to get connected nodes from.

        :return: A list of nodes connected to a node.

        :raises KeyError: Raised if the node is not in the graph.
        """
        if value in self.__nodes.keys():
            return self.__nodes[value]
        else:
            raise KeyError("Node not found.")

    def get_nodes(self):
        """
        Return list of nodes. O(1)

        :return: List of nodes present.
        """
        return self.__nodes.keys()

    def isAdjacent(self, source, destination):
        """
        Return True if the two nodes share an edge. O(n)

        :param source: First node of edge.
        :param destination: Second node of edge.

        :return: True if the two nodes share an edge, False otherwise.
        """
        return destination in self.__nodes[source] and source in self.__nodes[destination]

    def isPresent(self, node):
        """
        Return True if the node is present. O(n)

        :param node: The node to check.

        :return: True if the node is present, False otherwise.
        """
        return node in self.__nodes.keys()