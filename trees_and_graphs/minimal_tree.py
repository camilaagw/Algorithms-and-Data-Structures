"""Minimal tree: Given a sorted (increasing order) array with unique integer
 elements, write an algorithm to create a binary seach tree with minimal height"""

from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = f'{self.value}%3B'
        if self.left:
            res += f'{self.value}-%3E{self.left.value}%3B'
            res += str(self.left)
            if not self.right:
                res += f'{self.value}-%3EX{self.value}%3B'
                res += f'X{self.value}%5Bshape%3Dpoint%5D'
        if self.right:
            if not self.left:
                res += f'{self.value}-%3EX{self.value}%3B'
                res += f'X{self.value}%5Bshape%3Dpoint%5D'
            res += f'{self.value}-%3E{self.right.value}%3B'
            res += str(self.right)
        return res


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f'https://dreampuf.github.io/GraphvizOnline/#digraph%20A%20%7B' \
               f'{self.root or ""}%7D'

    @staticmethod
    def from_sorted_list(array: List[int]):
        """
        Create a binary seach tree with minimal heigh
        :param array: Sorted List of integers
        :return: Binary search tree
        """

        def insert_node_value(arr: List[int], start: int, end: int):
            node = None
            n = len(arr[start:end])
            if n:
                middle = n // 2 + start
                node = Node(arr[middle])
                node.left = insert_node_value(arr, start, middle)
                node.right = insert_node_value(arr, middle + 1, end)
            return node

        tree = Tree()
        tree.root = insert_node_value(array, start=0, end=len(array))

        return tree


if __name__ == "__main__":
    # Print an artificial tree
    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(7)
    root.right.right = Node(9)
    tree = Tree()
    tree.root = root
    print(tree)

    # Visually test the method from_sorted_list
    print(Tree.from_sorted_list([]))
    print(Tree.from_sorted_list([1]))
    print(Tree.from_sorted_list([1, 2]))
    print(Tree.from_sorted_list([1, 2, 3]))
    print(Tree.from_sorted_list(list(range(45))))
