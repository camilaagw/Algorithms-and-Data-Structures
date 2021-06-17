"""Is a binary tree balanced?"""

from tree_base import Tree, Node
from typing import Tuple


def is_balanced(tree: Tree) -> bool:
    def helper(node: Node) -> Tuple[bool, int]:
        """Returns a tuple with:
        - A boolean indicating if the tree formed the node is balanced
        - An integer indicating the depth of the tree (-1 if it is unbalanced)
        """
        if not node:
            return True, 0
        left_balanced, left_depth = helper(node.left)
        if not left_balanced:
            return False, -1
        right_balanced, right_depth = helper(node.right)
        balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
        return balanced, max(left_depth, right_depth) + 1
    balanced_flag, _ = helper(tree.root)
    return balanced_flag


if __name__ == "__main__":
    tree = Tree()
    # Print an artificial tree
    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    tree.root = root
    assert is_balanced(tree)

    root.left.left.left = Node(1)
    tree.root = root
    assert not is_balanced(tree)

