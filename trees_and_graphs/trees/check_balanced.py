"""Is a binary tree balanced?"""

from tree_base import Tree, Node
from typing import Tuple


def is_balanced(tree: Tree) -> bool:
    def helper(node: Node) -> Tuple[bool, int]:
        if not node:
            return True, 0
        left_balanced, left_depth = helper(node.left)
        if not left_balanced:
            return False, -1
        right_balanced, right_depth = helper(node.right)
        depth = max(left_depth, right_depth) + 1
        balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
        return balanced, depth
    balanced_flag, _ = helper(tree.root)
    return balanced_flag


def _depth(node: Node) -> int:
    if not node:
        return 0
    left_depth = _depth(node.left)
    right_depth = _depth(node.right)
    return max(left_depth, right_depth) + 1


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

