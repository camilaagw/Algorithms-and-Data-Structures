"""Write an algorithm to find the next node, in order successor of a given node
in a binary search tree. You may assume that each node has a parent"""

from typing import List, Optional
from tree_base import Node


class NodeWithParent(Node):
    def __init__(self, value: int, parent):
        super().__init__(value)
        self.parent = parent

    def next(self):
        if self.right:
            current_node = self.right.left_most_node()
        else:
            current_node = self.parent
            while current_node and self.value > current_node.value:
                current_node = current_node.parent

        return current_node

    def left_most_node(self):
        current_node = self
        while current_node.left:
            current_node = current_node.left
        return current_node

    def __str__(self):
        res = super().__str__()
        if self.parent:
            res += f'{self.value}-%3E{self.parent.value}%3B'
        return res


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f'https://dreampuf.github.io/GraphvizOnline/#digraph%20A%20%7B' \
               f'{self.root or ""}%7D'

    def left_most_node(self):
        if self.root:
            return self.root.left_most_node()

    @staticmethod
    def from_sorted_list(array: List[int]):
        """
        Create a binary search tree with minimal height
        :param array: Sorted List of integers
        :return: Binary search tree
        """

        def insert_node_value(
                arr: List[int],
                start: int,
                end: int,
                parent_node: Optional[NodeWithParent]
        ):
            node = None
            n = len(arr[start:end])
            if n:
                middle = n // 2 + start
                node = NodeWithParent(arr[middle], parent_node)
                node.left = insert_node_value(arr, start, middle, node)
                node.right = insert_node_value(arr, middle + 1, end, node)
            return node

        tree = Tree()
        tree.root = insert_node_value(array, start=0, end=len(array), parent_node=None)

        return tree


if __name__ == "__main__":
    for n in [20, 30, 40]:
        tree = Tree.from_sorted_list(list(range(n)))
        node = tree.left_most_node()
        values = [node.value]
        node = node.next()
        while node:
            values.append(node.value)
            node = node.next()
        assert values == list(range(n))
