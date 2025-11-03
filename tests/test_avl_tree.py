import pytest
from structures.avl_tree import AVLTree, AVLNode

def get_inorder_values(root):
    """Helper to get inorder traversal as list for easy assertion."""
    if root is None:
        return []
    return get_inorder_values(root.left) + [root.value] + get_inorder_values(root.right)


def test_add_single_node():
    tree = AVLTree()
    tree.add_node(10)
    assert tree.root.value == 10
    assert tree.root.balance_factor == 0
    assert tree.root.get_height() == 1


def test_duplicate_insert_raises():
    tree = AVLTree()
    tree.add_node(10)
    with pytest.raises(ValueError):
        tree.add_node(10)


def test_left_left_rotation():
    """
    Inserting in descending order should trigger LL rotation.
    """
    tree = AVLTree()
    for val in [30, 20, 10]:  # LL imbalance at 30
        tree.add_node(val)

    root = tree.root
    assert root.value == 20  # Root should rebalance
    assert get_inorder_values(root) == [10, 20, 30]
    assert root.left.value == 10
    assert root.right.value == 30


def test_right_right_rotation():
    """
    Inserting in ascending order should trigger RR rotation.
    """
    tree = AVLTree()
    for val in [10, 20, 30]:  # RR imbalance at 10
        tree.add_node(val)

    root = tree.root
    assert root.value == 20
    assert get_inorder_values(root) == [10, 20, 30]
    assert root.left.value == 10
    assert root.right.value == 30


def test_left_right_rotation():
    """
    Insert pattern: root-left-right triggers LR rotation.
    """
    tree = AVLTree()
    for val in [30, 10, 20]:  # LR case at 30
        tree.add_node(val)

    root = tree.root
    assert root.value == 20
    assert get_inorder_values(root) == [10, 20, 30]
    assert root.left.value == 10
    assert root.right.value == 30


def test_right_left_rotation():
    """
    Insert pattern: root-right-left triggers RL rotation.
    """
    tree = AVLTree()
    for val in [10, 30, 20]:  # RL case at 10
        tree.add_node(val)

    root = tree.root
    assert root.value == 20
    assert get_inorder_values(root) == [10, 20, 30]
    assert root.left.value == 10
    assert root.right.value == 30


def test_balance_factors_update_propagates():
    tree = AVLTree()
    for val in [10, 5, 15, 2, 7, 12, 17]:
        tree.add_node(val)
    root = tree.root
    # Should remain balanced after all insertions
    assert root.balance_factor in [-1, 0, 1]
    assert root.left.balance_factor in [-1, 0, 1]
    assert root.right.balance_factor in [-1, 0, 1]


def test_parent_pointers_maintained():
    tree = AVLTree()
    for val in [10, 5, 15, 2, 7, 12, 17]:
        tree.add_node(val)
    root = tree.root
    assert root.left.parent == root
    assert root.right.parent == root


def test_complex_sequence_balances_correctly():
    """
    Add nodes in a complex order that triggers multiple rebalances.
    """
    tree = AVLTree()
    vals = [10, 20, 30, 40, 50, 25]
    for v in vals:
        tree.add_node(v)

    root = tree.root
    assert get_inorder_values(root) == sorted(vals)
    # Should remain balanced
    def check_balanced(node):
        if not node:
            return
        assert node.balance_factor in [-1, 0, 1]
        check_balanced(node.left)
        check_balanced(node.right)
    check_balanced(root)

# Below contains the same tests but with trees mirrored about the root.
def test_mirror_left_left_rotation():
    tree = AVLTree()
    for val in [-30, -20, -10]:  # LL imbalance at 30
        tree.add_node(val)
    root = tree.root
    assert root.value == -20  # Root should rebalance
    assert get_inorder_values(root) == [-30, -20, -10]
    assert root.left.value == -30
    assert root.right.value == -10


def test_mirror_right_right_rotation():
    tree = AVLTree()
    for val in [-10, -20, -30]:  # RR imbalance at 10
        tree.add_node(val)

    root = tree.root
    assert root.value == -20
    assert get_inorder_values(root) == [-30, -20, -10]
    assert root.left.value == -30
    assert root.right.value == -10


def test_mirror_left_right_rotation():
    tree = AVLTree()
    for val in [-30, -10, -20]:  # LR case at 30
        tree.add_node(val)
    root = tree.root
    assert root.value == -20
    assert get_inorder_values(root) == [-30, -20, -10]
    assert root.left.value == -30
    assert root.right.value == -10


def test_mirror_right_left_rotation():
    tree = AVLTree()
    for val in [-10, -30, -20]:  # RL case at 10
        tree.add_node(val)
    root = tree.root
    assert root.value == -20
    assert get_inorder_values(root) == [-30, -20, -10]
    assert root.left.value == -30
    assert root.right.value == -10


def test_mirror_balance_factors_update_propagates():
    tree = AVLTree()
    for val in [-10, -5, -15, -2, -7, -12, -17]:
        tree.add_node(val)
    root = tree.root
    assert root.balance_factor in [-1, 0, 1]
    assert root.left.balance_factor in [-1, 0, 1]
    assert root.right.balance_factor in [-1, 0, 1]


def test_mirror_parent_pointers_maintained():
    tree = AVLTree()
    for val in [-10, -5, -15, -2, -7, -12, -17]:
        tree.add_node(val)
    root = tree.root
    assert root.left.parent == root
    assert root.right.parent == root


def test_mirror_complex_sequence_balances_correctly():
    tree = AVLTree()
    vals = [-10, -20, -30, -40, -50, -25]
    for v in vals:
        tree.add_node(v)
    root = tree.root
    assert get_inorder_values(root) == sorted(vals)
    def check_balanced(node):
        if not node:
            return
        assert node.balance_factor in [-1, 0, 1]
        check_balanced(node.left)
        check_balanced(node.right)
    check_balanced(root)

def build_balanced_tree():
    """
    Helper: builds a perfectly balanced tree.
                30
              /    \
            20      40
           /  \    /  \
         10  25  35  50
    """
    tree = AVLTree()
    for val in [30, 20, 40, 10, 25, 35, 50]:
        tree.add_node(val)
    return tree

def test_remove_from_empty_tree_raises():
    tree = AVLTree()
    with pytest.raises(ValueError, match="Node does not exist"):
        tree.remove_node(10)

def test_remove_leaf_node():
    tree = build_balanced_tree()
    tree.remove_node(10)  # remove leaf

    # 10 should be gone
    assert tree.root.left.left is None
    # Root should remain same
    assert tree.root.value == 30

def test_remove_node_with_right_child():
    tree = AVLTree()
    for v in [10, 20, 30]:
        tree.add_node(v)  # forms right-skewed tree
    tree.remove_node(20)
    # 10 -> 30 after rebalance
    assert tree.root.value in [10, 20, 30]  # rebalanced tree valid
    # 20 must not exist
    with pytest.raises(ValueError):
        tree.remove_node(20)

def test_remove_node_with_left_child():
    tree = AVLTree()
    for v in [30, 20, 10]:
        tree.add_node(v)
    tree.remove_node(20)
    # 10 or 30 is root depending on rebalance
    assert tree.root.value in [10, 30]
    # Ensure 20 gone
    with pytest.raises(ValueError):
        tree.remove_node(20)

def test_remove_node_with_two_children():
    tree = build_balanced_tree()
    tree.remove_node(20)  # has left=10, right=25
    # check replacement occurred correctly
    found = tree.root.left
    assert found.value in [10, 25]
    assert tree.find_node(20) is None

def test_remove_root_with_two_children():
    tree = build_balanced_tree()
    tree.remove_node(30)
    # Root should update (successor 35 or 40 typically)
    assert tree.root.value in [35, 40, 25]
    # Old root gone
    assert tree.find_node(30) is None

def test_remove_until_empty():
    tree = AVLTree()
    for v in [10, 5, 15]:
        tree.add_node(v)
    for v in [5, 15, 10]:
        tree.remove_node(v)
    assert tree.root is None

def test_rebalance_after_deletion():
    tree = AVLTree()
    for v in [50, 30, 70, 20, 40, 60, 80, 10]:
        tree.add_node(v)

    # This removal causes imbalance requiring rotation
    tree.remove_node(80)

    # Ensure tree is still balanced (no |bf| > 1)
    def is_balanced(node):
        if not node:
            return True
        if abs(node.balance_factor) > 1:
            return False
        return is_balanced(node.left) and is_balanced(node.right)

    assert is_balanced(tree.root)

def test_remove_nonexistent_node():
    tree = build_balanced_tree()
    with pytest.raises(ValueError, match="Node does not exist"):
        tree.remove_node(999)
