"""Given a pair of node values in a tree, find the first ancestor of both"""

from tree_base import Tree, Node
from typing import Set, List, Optional


def get_first_ancestor(values: List[int], tree: Tree) -> Optional[int]:

    ancestor = None

    def helper(node: Node) -> Set[int]:
        """Returns a set with the values seen so far and
        sets the ancestor the first time it sees both children"""
        nonlocal ancestor
        if not node:
            return set()
        result = helper(node.left) | helper(node.right)
        if node.value in values:
            result.add(node.value)

        if len(result) == 2 and not ancestor:
            ancestor = node.value
        return result

    helper(tree.root)
    return ancestor


if __name__ == "__main__":
    my_tree = Tree.from_sorted_list(list(range(45)))
    assert get_first_ancestor([11, 34], my_tree) == 22, get_first_ancestor([11, 34], my_tree)
    assert get_first_ancestor([12, 21], my_tree) == 17
    assert get_first_ancestor([40, 37], my_tree) == 40
    assert get_first_ancestor([1, 8], my_tree) == 5
    assert get_first_ancestor([5, 0], my_tree) == 5
    assert get_first_ancestor([5, 9], my_tree) == 5
    assert get_first_ancestor([36, 39], my_tree) == 37
    assert get_first_ancestor([50, 22], my_tree) is None
    assert get_first_ancestor([22, 22], my_tree) is None



