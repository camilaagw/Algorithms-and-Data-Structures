"""Determine if a binary tree T2 is a subtree of a binary tree T1"""
from tree_base import Tree, Node


def is_subtree(t1: Tree, t2: Tree) -> bool:
    """Return True if t2 is a subtree of t1, otherwise returns False"""
    if not t2.root:
        return True

    def find_subtree_starting_from(node: Node) -> bool:
        if not node:
            return False
        return equal_trees(node, t2.root) or \
               find_subtree_starting_from(node.left) or \
               find_subtree_starting_from(node.right)

    return find_subtree_starting_from(t1.root)


def equal_trees(root1: Node, root2: Node) -> bool:
    """Return True if the trees under root1 and root2 are equal"""
    if not root1 and not root2:
        return True
    if not root1 or not root2 or root1.value != root2.value:
        return False
    return equal_trees(root1.left, root2.left) and \
           equal_trees(root1.right, root2.right)


if __name__ == "__main__":
    my_tree = Tree.from_sorted_list(list(range(1, 20)))
    my_tree2 = Tree.from_sorted_list(list(range(1, 21)))

    root = Node(18)
    root.left = Node(17)
    root.right = Node(19)
    root.left.left = Node(16)
    my_tree3 = Tree()
    my_tree3.root = root

    root = Node(18)
    root.left = Node(17)
    root.right = Node(19)
    my_tree4 = Tree()
    my_tree4.root = root

    assert equal_trees(my_tree.root, my_tree.root)
    assert not equal_trees(my_tree.root, my_tree2.root)

    assert is_subtree(my_tree, my_tree)
    assert is_subtree(my_tree, my_tree)
    assert is_subtree(my_tree, my_tree3)
    assert not is_subtree(my_tree, my_tree4)
