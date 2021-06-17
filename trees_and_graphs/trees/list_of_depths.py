"""Given a binary tree design an algorithm which creates a list of all the
nodes at each depth (e.g if you have a tree with depth D, you'll have D  lists"""

from typing import List
from tree_base import Tree, Node


def tree_to_list_by_depth(tree: Tree) -> List[List[Node]]:
    """Iterative version"""
    main_list = []
    current_list = [tree.root] if tree.root else None
    while current_list:
        main_list.append(current_list)
        temp_list = []
        for node in current_list:
            if node.left:
                temp_list.append(node.left)
            if node.right:
                temp_list.append(node.right)
        current_list = temp_list

    return main_list


def tree_to_list_by_depth_v2(tree: Tree) -> List[List[Node]]:
    """Recursive version"""
    main_list = []

    def traverse_node(node: Node, depth: int):
        if node:
            if depth > len(main_list) - 1:
                main_list.append([])
            main_list[depth].append(node)
            traverse_node(node.left, depth + 1)
            traverse_node(node.right, depth + 1)

    traverse_node(tree.root, 0)
    return main_list


if __name__ == "__main__":
    my_tree = Tree.from_sorted_list(list(range(20)))
    for func in [tree_to_list_by_depth, tree_to_list_by_depth_v2]:
        result = [
            list(map(lambda x: x.value, _list))
            for _list in func(my_tree)
        ]
        assert result == [[10], [5, 15], [2, 8, 13, 18], [1, 4, 7, 9, 12, 14, 17, 19], [0, 3, 6, 11, 16]]



