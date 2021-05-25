""" A BST was created by traversing through an array from left to right and inserting
each element. Given a BST with distinct elements, print all possible arrays that
could have led to this tree
"""
from tree_base import Tree, Node


def get_construction_lists(tree: Tree):
    construction_list = []

    def helper(current_list: list, next_nodes: list):
        for node in next_nodes:
            new_next_nodes = next_nodes.copy()
            new_next_nodes.remove(node)
            if node.right:
                new_next_nodes.append(node.right)
            if node.left:
                new_next_nodes.append(node.left)
            helper(current_list + [node.value], new_next_nodes)
        if not next_nodes:
            construction_list.append(current_list)

    helper([], [tree.root])
    return construction_list


# def get_construction_lists(tree: Tree):
#     construction_list = []
#
#     def helper(current_list: List, node: Node):
#         if node:
#             helper(current_list + [node.value], node.left)
#             helper(current_list + [node.value], node.right)
#         else:
#             construction_list.append(current_list)
#
#     helper([], tree.root)
#     return construction_list


if __name__ == "__main__":

    my_tree = Tree.from_sorted_list(list(range(1, 4)))
    assert get_construction_lists(my_tree) == [
        [2, 3, 1],
        [2, 1, 3]
    ], get_construction_lists(my_tree)

    my_tree = Tree.from_sorted_list(list(range(1, 6)))
    assert get_construction_lists(my_tree) == [
        [3, 5, 2, 4, 1],
        [3, 5, 2, 1, 4],
        [3, 5, 4, 2, 1],
        [3, 2, 5, 1, 4],
        [3, 2, 5, 4, 1],
        [3, 2, 1, 5, 4]
    ]


    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    tree = Tree()
    tree.root = root
    assert get_construction_lists(tree) == [
        [4, 5, 2, 3, 1],
        [4, 5, 2, 1, 3],
        [4, 2, 5, 3, 1],
        [4, 2, 5, 1, 3],
        [4, 2, 3, 5, 1],
        [4, 2, 3, 1, 5],
        [4, 2, 1, 5, 3],
        [4, 2, 1, 3, 5]
    ]






