"""Given a binary tree in which each node contains an integer value
(positive or negative), count the number of paths that sum to a given value.
The path must go downwards and does not need to start or end at the root or a
leaf
"""
from collections import Counter
import time

from tree_base import Tree, Node


def num_paths_with_target_sum(tree: Tree, target: int) -> int:
    """Brute-force version"""
    def helper(node: Node) -> int:
        if not node:
            return 0
        return target_sum(node) + helper(node.left) + helper(node.right)

    def target_sum(node: Node, acc: int = 0) -> int:
        if not node:
            return 0
        next_acc = node.value + acc
        return int(next_acc == target) + \
               target_sum(node.left, next_acc) + \
               target_sum(node.right, next_acc)

    return helper(tree.root)


def num_paths_with_target_sum_v2(tree: Tree, target: int) -> int:
    """Optimized version :)"""
    acc_counter = Counter([0])

    def target_sum(node: Node, acc: int) -> int:
        if not node:
            return 0
        next_acc = node.value + acc
        count = acc_counter[next_acc - target]
        acc_counter[next_acc] += 1
        result = count + \
               target_sum(node.left, next_acc) + \
               target_sum(node.right, next_acc)
        acc_counter[next_acc] -= 1

        return result
    return target_sum(tree.root, acc=0)


if __name__ == "__main__":
    bst = Tree.from_sorted_list(list(range(10)))
    bst_big = Tree.from_sorted_list(list(range(10000000)))

    for func in [num_paths_with_target_sum, num_paths_with_target_sum_v2]:
        assert func(bst, 8) == 3
        assert func(bst, 3) == 3
        assert func(bst, 13) == 2
        start = time.time()
        func(bst_big, 15)
        print(time.time() - start)
