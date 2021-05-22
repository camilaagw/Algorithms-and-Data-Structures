"""Write a function that takes a graph and returns the list(s)
of connected nodes"""
from graph_base import Graph, breath_first_list
from typing import List


def get_connected_nodes(graph: Graph) -> List[List[int]]:
    subgraphs_list = []
    nodes = set(range(graph.size))
    while nodes:
        nodes_list = []
        start_node = nodes.pop()
        breath_first_list(graph, start_node, lambda x: nodes_list.append(x))
        subgraphs_list.append(nodes_list)
        nodes.difference_update(nodes_list)
    return subgraphs_list


if __name__ == "__main__":
    graph1 = Graph.non_directed_from_edges(
        size=7,
        edges=[(0, 1), (1, 2), (2, 0), (2, 3), (4, 6), (5, 4), (6, 5)]
    )
    assert get_connected_nodes(graph1) == [[0, 1, 2, 3], [4, 5, 6]]

    graph2 = Graph.non_directed_from_edges(
        size=3,
        edges=[]
    )
    assert get_connected_nodes(graph2) == [[0], [1], [2]]

    graph3 = Graph.non_directed_from_edges(
        size=7,
        edges=[(0, 1), (2, 3), (6, 5)]
    )
    assert get_connected_nodes(graph3) == [[0, 1], [2, 3], [4], [5, 6]]


