import pytest
from structures.dense_graph import DenseGraph

@pytest.fixture
def populated_graph():
    graph = DenseGraph(6)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    return graph

def test_add_node():
    graph = DenseGraph(3)
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    assert graph.get_nodes() == [0, 1, 2]
    with pytest.raises(KeyError, match="Node already present."):
        graph.add_node(1)
    with pytest.raises(ValueError, match="Node value out of range."):
        graph.add_node(-1)
    with pytest.raises(ValueError, match="Node value out of range."):
        graph.add_node(4)

def test_add_edge(populated_graph):
    assert populated_graph.get_connected_nodes(1) == [2, 3]
    assert populated_graph.get_connected_nodes(2) == [1]
    assert populated_graph.get_connected_nodes(3) == [1, 4]
    assert populated_graph.get_connected_nodes(4) == [3]
    with pytest.raises(KeyError, match="Edge already present."):
        populated_graph.add_edge(2, 1)
    with pytest.raises(ValueError, match="Cannot add an edge between same node."):
        populated_graph.add_edge(1, 1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.add_edge(4, -1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.add_edge(6, 1)
    with pytest.raises(KeyError, match="Node not found."):
        populated_graph.add_edge(1, 5)

def test_remove_node(populated_graph):
    populated_graph.remove_node(1)
    assert populated_graph.get_nodes() == [2, 3, 4]
    assert populated_graph.get_connected_nodes(2) == []
    assert populated_graph.get_connected_nodes(3) == [4]
    populated_graph.remove_node(4)
    assert populated_graph.get_nodes() == [2, 3]
    assert populated_graph.get_connected_nodes(3) == []
    populated_graph.remove_node(3)
    with pytest.raises(KeyError, match="Node not found."):
        populated_graph.remove_node(1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.remove_node(-1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.remove_node(6)

def test_remove_edge(populated_graph):
    populated_graph.remove_edge(1, 2)
    assert populated_graph.get_connected_nodes(1) == [3]
    assert populated_graph.get_connected_nodes(2) == []
    populated_graph.remove_edge(4, 1)
    assert populated_graph.get_connected_nodes(4) == [3]
    populated_graph.remove_edge(4, 4)
    assert populated_graph.get_connected_nodes(4) == [3]
    with pytest.raises(KeyError, match="Node not found."):
        populated_graph.remove_edge(1, 5)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.remove_edge(4, -1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.remove_edge(4, 7)

def test_get_connected_nodes(populated_graph):
    assert populated_graph.get_connected_nodes(1) == [2, 3]
    assert populated_graph.get_connected_nodes(4) == [3]
    with pytest.raises(KeyError, match="Node not found."):
        populated_graph.get_connected_nodes(5)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.get_connected_nodes(-1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.get_connected_nodes(7)

def test_get_nodes(populated_graph):
    assert populated_graph.get_nodes() == [1, 2, 3, 4]

def test_is_adjacent(populated_graph):
    assert populated_graph.isAdjacent(1, 2) == True
    assert populated_graph.isAdjacent(1, 4) == False
    assert populated_graph.isAdjacent(1, 1) == False
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.isAdjacent(4, -1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.isAdjacent(4, 7)

def test_is_present(populated_graph):
    assert populated_graph.isPresent(1) == True
    assert populated_graph.isPresent(5) == False
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.isPresent(-1)
    with pytest.raises(ValueError, match="Node value out of range."):
        populated_graph.isPresent(7)