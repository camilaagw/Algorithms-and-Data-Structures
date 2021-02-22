"""Route between nodes (Book 4.1)"""
from collections import deque
from graph_base import Graph


def route_exists(graph: Graph, from_node, to_node) -> bool:
    queue = deque()
    enqueued = set()

    queue.append(from_node)
    enqueued.add(from_node)
    while queue:
        current_node = queue.popleft()
        if current_node == to_node:
            return True
        for child in graph.children(current_node):
            if child not in enqueued:
                queue.append(child)
                enqueued.add(child)

    return False


if __name__ == "__main__":

    graph1 = Graph.from_edges(
        size=6,
        edges=[(0, 1), (0, 4), (0, 5), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4)]
    )
    assert route_exists(graph1, 0, 2)
    assert not route_exists(graph1, 2, 5)
    assert not route_exists(graph1, 5, 3)

    graph2 = Graph(3)
    graph2.add_edge(0, 1)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 0)
    assert route_exists(graph2, 0, 2)