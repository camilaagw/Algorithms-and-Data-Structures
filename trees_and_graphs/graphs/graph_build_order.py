"""You are given a list of projects and a list of dependencies
(which is a list of pairs of projects, where the 1st project is
dependent on the 2nd project. All of a project's dependencies
must be built before the project is. Find a build order that will allow
the projects to be built.
If there is no valid build order, return None
"""

from typing import List, Tuple
from collections import defaultdict


class Graph:

    def __init__(self):
        self.removed_nodes = set()
        self.edges = defaultdict(set)
        self.rev_edges = defaultdict(set)

    def is_empty(self):
        return len(self.removed_nodes) == len(self.edges.keys())

    def add_edge(self, from_, to_):
        self.edges[from_].add(to_)
        self.rev_edges[to_].add(from_)
        self.edges[to_] = self.edges[to_]

    def remove_node(self, node):
        self.removed_nodes.add(node)

    def following_nodes(self, node):
        if node not in self.removed_nodes:
            for to_ in self.edges[node]:
                if to_ not in self.removed_nodes:
                    yield to_

    def has_following_nodes(self, node):
        if node not in self.removed_nodes:
            for to_ in self.edges[node]:
                if to_ not in self.removed_nodes:
                    return True
        return False


def get_build_order_v1(edges: List[Tuple[int, int]]):
    """Implementation by removing dependency-less tasks"""
    possible_origins = set()
    edges_dict = defaultdict(list)
    num_incoming_edges = defaultdict(int)
    for from_, to_ in edges:
        num_incoming_edges[to_] += 1
        edges_dict[from_].append(to_)
        possible_origins.add(from_)

    build_order = []
    while edges_dict:
        origins = set()
        for origin in possible_origins:
            if not num_incoming_edges[origin]:
                origins.add(origin)

        if not origins:
            return None

        build_order.extend(origins)

        next_origins = set()
        for origin in origins:
            next_origins.update(edges_dict[origin])
            for temp in edges_dict[origin]:
                num_incoming_edges[temp] -= 1
            del edges_dict[origin]
        possible_origins = next_origins

    build_order.extend(possible_origins)

    return build_order


def get_build_order(edges: List[Tuple[int, int]]):
    """Implementation with depth first search"""
    graph = Graph()
    origins = set()
    destinations = set()
    for from_, to_ in edges:
        graph.add_edge(from_, to_)
        origins.add(from_)
        destinations.add(to_)
    origins.difference_update(destinations)

    visited = set()
    build_order = []

    def dfs(node: int):
        visited.add(node)
        for node_to in graph.following_nodes(node):
            if node_to not in visited:
                dfs(node_to)
        if not graph.has_following_nodes(node):
            build_order.append(node)
            graph.remove_node(node)

    for origin in origins:
        dfs(origin)

    if not graph.is_empty():
        return None
    if build_order:
        build_order.reverse()

    return build_order


if __name__ == "__main__":
    assert get_build_order([(1, 1)]) is None
    assert get_build_order([(1, 2), (2, 3), (3, 1)]) is None
    assert get_build_order([(1, 2), (2, 3), (3, 2), (3, 4)]) is None
    assert get_build_order(
        [(1, 3), (1, 2), (2, 3), (2, 4), (3, 4), (4, 5)]) == [1, 2, 3, 4, 5]

    assert get_build_order(
        [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (6, 7)]
    ) in [[1, 6, 2, 7, 3, 4], [6, 7, 1, 2, 3, 4]]
