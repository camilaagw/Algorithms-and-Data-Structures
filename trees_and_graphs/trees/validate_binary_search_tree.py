"""Implement a function to check if a binary search tree"""

from tree_base import Tree, Node
from typing import Tuple


def is_binary_search_tree(tree: Tree) -> bool:
    def get_limit_values(node: Node) -> Tuple[bool, int, int]:
        if not node:
            return True, 2 ** 32, -2 ** 32
        val = node.value
        balanced_r, min_r, max_r = get_limit_values(node.right)
        balanced_l, min_l, max_l = get_limit_values(node.left)
        balanced = balanced_r and balanced_l and max_l < val < min_r
        return balanced, min(val, min_l, min_r), max(val, max_l, max_r)

    return get_limit_values(tree.root)[0]


def is_binary_search_tree_v2(tree: Tree) -> bool:
    def within_limits(node: Node, min_: int, max_: int) -> bool:
        return (not node) or \
               min_ < node.value < max_ and \
               within_limits(node.left, min_, node.value) and \
               within_limits(node.right, node.value, max_)

    return within_limits(tree.root, -2 ** 32, 2 ** 32)


def _get_limit_values(node: Node) -> Tuple[int, int]:
    if not node:
        return 2 ** 32, -2 ** 32
    val = node.value
    min_r, max_r = _get_limit_values(node.right)
    min_l, max_l = _get_limit_values(node.left)
    return min(val, min_l, min_r), max(val, max_l, max_r)


if __name__ == "__main__":
    unbalanced_tree = Tree.from_sorted_list([12, 13, 14, 1, 2, 3, 4, 5])
    balanced_tree = Tree.from_sorted_list(list(range(20)))

    for func in [is_binary_search_tree, is_binary_search_tree_v2]:
        assert not func(unbalanced_tree)
        assert func(balanced_tree)
