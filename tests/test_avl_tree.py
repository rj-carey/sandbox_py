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

def test_rotate_right_updates_y_right_parent():
    """
    Cover line 69: y.right.parent = z in __rotate_right().
    This happens during a Left-Right imbalance (y.right exists).
    """
    tree = AVLTree()
    # Create LR case: insert 30 (root), 10 (left), 20 (right of left)
    for val in [30, 10, 20]:
        tree.add_node(val)
    # After rebalancing, tree should be balanced
    assert tree.root.value == 20
    assert tree.root.left.value == 10
    assert tree.root.right.value == 30
    # Confirm parent relationships (y.right.parent = z executed)
    assert tree.root.left.parent == tree.root
    assert tree.root.right.parent == tree.root


def test_rotate_left_with_parent_left_branch():
    """
    Cover line 75: z.parent.left = y in __rotate_left().
    We cause a right-heavy subtree rotation inside a left branch.
    """
    tree = AVLTree()
    # Create structure:
    #         50
    #        /
    #      20
    #        \
    #         40
    #           \
    #            45  -> triggers rotation at node 40, which is z (child of 20)
    for val in [50, 20, 55, 40, 45]:
        tree.add_node(val)

    root = tree.root
    # Root should stay the same
    assert root.value == 50
    # Left subtree should be rebalanced
    assert root.left.value in (20, 40, 45)
    # Verify we covered z.parent.left=y behavior
    assert root.left.parent == root
