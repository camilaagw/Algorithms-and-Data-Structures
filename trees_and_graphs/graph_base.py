"""
1 . Implement graph traversals using
- Depth First Search
- Breath First Search

Implement the graph as an adjacency list"""
from typing import List, Tuple
from collections import deque


class Graph:

    def __init__(self, size: int):
        self.size = size
        self.adjacency_list = [set() for _ in range(self.size)]

    @staticmethod
    def from_edges(size: int, edges: List[Tuple[int, int]]):
        graph = Graph(size)
        for from_node, to_node in edges:
            graph.add_edge(from_node, to_node)
        return graph

    def add_edge(self, from_node: int, to_node: int):
        self.adjacency_list[from_node].add(to_node)

    def children(self, node:int) -> List[int]:
        return self.adjacency_list[node]


def depth_first_list(graph: Graph, start_node: int, visit):
    visited = set()

    def traverse(node):
        visit(node)
        visited.add(node)
        for child in graph.children(node):
            if child not in visited:
                traverse(child)

    traverse(start_node)


def breath_first_list(graph: Graph, start_node: int, visit):
    queue = deque()
    enqueued = set()

    queue.append(start_node)
    enqueued.add(start_node)
    while queue:
        current_node = queue.popleft()  # Replace to pop ("right") to convert it do DFS ;)
        visit(current_node)
        for child in graph.children(current_node):
            if child not in enqueued:
                queue.append(child)
                enqueued.add(child)


def test_list_graph(graph, expected, func):
    nodes_list = []
    func(graph, 0, lambda x: nodes_list.append(x))
    assert nodes_list == expected, nodes_list


if __name__ == "__main__":

    graph1 = Graph.from_edges(
        size=6,
        edges=[(0, 1),  (0, 4), (0, 5), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4)]
    )
    test_list_graph(graph1, [0, 1, 3, 2, 4, 5], depth_first_list)
    test_list_graph(graph1, [0, 1, 4, 5, 3, 2], breath_first_list)

    graph2 = Graph(3)
    graph2.add_edge(0, 1)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 0)
    test_list_graph(graph2, [0, 1, 2], depth_first_list)
    test_list_graph(graph2, [0, 1, 2], breath_first_list)