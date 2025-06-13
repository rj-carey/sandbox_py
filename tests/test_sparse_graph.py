import pytest
from structures.sparse_graph import SparseGraph

@pytest.fixture
def populated_graph():
    graph = SparseGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    return graph

def test_add_node():
    graph = SparseGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    assert graph.get_nodes() == [1, 2, 3]
    with pytest.raises(KeyError, match="Node already present."):
        graph.add_node(1)

def test_add_edge(populated_graph):
    assert populated_graph.get_connected_nodes(1) == [2, 3]
    assert populated_graph.get_connected_nodes(2) == [1]
    assert populated_graph.get_connected_nodes(3) == [1, 4]
    assert populated_graph.get_connected_nodes(4) == [3]
    with pytest.raises(KeyError, match="Edge already present."):
        populated_graph.add_edge(2, 1)

def test_remove_node(populated_graph):
    populated_graph.remove_node(1)
    assert populated_graph.get_nodes() == [2, 3, 4]
    assert populated_graph.get_connected_nodes(2) == []
    assert populated_graph.get_connected_nodes(3) == [4]
    with pytest.raises(KeyError, match="Node not found."):
        populated_graph.remove_node(1)

def test_remove_edge(populated_graph):
    populated_graph.remove_edge(1, 2)
    assert populated_graph.get_connected_nodes(1) == [3]
    assert populated_graph.get_connected_nodes(2) == []
    with pytest.raises(KeyError, match="Node not found."):
        populated_graph.remove_edge(1, 5)

def test_get_connected_nodes(populated_graph):
    assert populated_graph.get_connected_nodes(1) == [2, 3]
    assert populated_graph.get_connected_nodes(4) == [3]
    with pytest.raises(KeyError, match="Node not found."):
        populated_graph.get_connected_nodes(5)

def test_get_nodes(populated_graph):
    assert populated_graph.get_nodes() == [1, 2, 3, 4]

def test_is_adjacent(populated_graph):
    assert populated_graph.isAdjacent(1, 2) == True
    assert populated_graph.isAdjacent(1, 4) == False

def test_is_present(populated_graph):
    assert populated_graph.isPresent(1) == True
    assert populated_graph.isPresent(5) == False