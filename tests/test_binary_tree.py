import pytest
from structures.binary_tree import BTNode, BinaryTree

# ------------------ BTNode Tests ------------------

def test_btnode_comparisons():
    a = BTNode(5)
    b = BTNode(10)
    c = BTNode(5)
    assert a == c
    assert a < b
    assert b > a

# ---------------- BinaryTree Add & Find ----------------

def test_add_and_find_single_node():
    tree = BinaryTree()
    tree.add_node(10)
    node = tree.find_node(10)
    assert node is not None
    assert node.value == 10

def test_add_multiple_and_find():
    tree = BinaryTree()
    for value in [20, 10, 30, 5, 15]:
        tree.add_node(value)
    assert tree.find_node(15).value == 15
    assert tree.find_node(99) is None

def test_add_duplicate_raises():
    tree = BinaryTree()
    tree.add_node(10)
    with pytest.raises(ValueError, match="Node already exists."):
        tree.add_node(10)

# ---------------- BinaryTree Remove ----------------

def test_remove_node_leaf():
    tree = BinaryTree()
    for v in [20, 10, 30]:
        tree.add_node(v)
    tree.remove_node(10)
    assert tree.find_node(10) is None

def test_remove_node_with_children():
    tree = BinaryTree()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        tree.add_node(v)
    tree.remove_node(30)
    assert tree.find_node(30) is None
    assert tree.find_node(20) is not None
    assert tree.find_node(40) is not None

def test_remove_node_one_subtree():
    tree = BinaryTree()
    for v in [5,4,3]:
        tree.add_node(v)
    tree.remove_node(4)
    assert tree.find_node(4) is None
    assert tree.find_node(5) is not None
    assert tree.find_node(3) is not None

def test_remove_node_deep_replacement():
    tree = BinaryTree()
    for v in [5,3,1,2, 4]:
        tree.add_node(v)
    tree.remove_node(3)
    assert tree.find_node(3) is None
    assert tree.find_node(5) is not None
    assert tree.find_node(2) is not None
    assert tree.find_node(1) is not None
    assert tree.find_node(4) is not None

def test_remove_node_deep_position_left():
    tree = BinaryTree()
    for v in [5,4,2,1,3]:
        tree.add_node(v)
    tree.remove_node(1)
    assert tree.find_node(1) is None
    assert tree.find_node(5) is not None
    assert tree.find_node(3) is not None
    assert tree.find_node(2) is not None
    assert tree.find_node(4) is not None

def test_remove_node_deep_position_right():
    tree = BinaryTree()
    for v in [1,2,4,3,5]:
        tree.add_node(v)
    tree.remove_node(5)
    assert tree.find_node(5) is None
    assert tree.find_node(1) is not None
    assert tree.find_node(3) is not None
    assert tree.find_node(2) is not None
    assert tree.find_node(4) is not None

def test_remove_root_node():
    tree = BinaryTree()
    for v in [10, 5, 15]:
        tree.add_node(v)
    tree.remove_node(10)
    assert tree.find_node(10) is None
    assert tree.find_node(5)
    assert tree.find_node(15)

def test_remove_nonexistent_node_raises():
    tree = BinaryTree()
    tree.add_node(10)
    with pytest.raises(ValueError, match="Node does not exist."):
        tree.remove_node(5)
    with pytest.raises(ValueError, match="Node does not exist."):
        tree.remove_node(20)

def test_remove_from_empty_raises():
    tree = BinaryTree()
    with pytest.raises(ValueError, match="The tree is empty."):
        tree.remove_node(42)

# ---------------- Traversal Tests ----------------

def test_preorder_traversal(capsys):
    tree = BinaryTree()
    for v in [10, 5, 15]:
        tree.add_node(v)
    tree.traverse(BinaryTree.PREORDER)
    out, _ = capsys.readouterr()
    assert out == "10, 5, 15, "

def test_inorder_traversal(capsys):
    tree = BinaryTree()
    for v in [10, 5, 15]:
        tree.add_node(v)
    tree.traverse(BinaryTree.INORDER)
    out, _ = capsys.readouterr()
    assert out == "5, 10, 15, "

def test_postorder_traversal(capsys):
    tree = BinaryTree()
    for v in [10, 5, 15]:
        tree.add_node(v)
    tree.traverse(BinaryTree.POSTORDER)
    out, _ = capsys.readouterr()
    assert out == "5, 15, 10, "

def test_levelorder_traversal(capsys):
    tree = BinaryTree()
    for v in [10, 5, 15]:
        tree.add_node(v)
    tree.traverse(BinaryTree.LEVELORDER)
    out, _ = capsys.readouterr()
    assert out == "10, 5, 15, "

def test_traverse_invalid_mode_raises():
    tree = BinaryTree()
    with pytest.raises(ValueError, match="Invalid mode."):
        tree.traverse(99)

# ---------------- Height and Size ----------------

def test_tree_height():
    tree = BinaryTree()
    assert tree.get_height() == 0
    tree.add_node(10)
    tree.add_node(5)
    tree.add_node(3)
    assert tree.get_height() == 3  # 10 -> 5 -> 3

def test_tree_size():
    tree = BinaryTree()
    assert tree.get_size() == 0
    for v in [10, 5, 15, 3, 7]:
        tree.add_node(v)
    assert tree.get_size() == 5
