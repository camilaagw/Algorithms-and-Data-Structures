"""
Given a grid of colors describing a map of countries, where a contiguous blob
of colour represents a country, count the number of countries on the map.
"""

from graph_base import Graph
from graph_connected_nodes import get_connected_nodes
from typing import List
from collections import deque


def get_num_countries(matrix: List[List[int]]) -> int:
    """ Given a matrix represented as a List of Lists
    find the the number of countries, using a graph
    data structure"""
    graph = _map_to_graph(matrix)
    return len(get_connected_nodes(graph))


def _map_to_graph(matrix: List[List[int]]) -> Graph:
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    graph = Graph(n_rows * n_cols)

    for i in range(n_rows):
        for j in range(n_cols):
            if i > 0 and matrix[i][j] == matrix[i - 1][j]:
                n1, n2 = i * n_cols + j, (i - 1) * n_cols + j
                graph.add_edge(n1, n2)
                graph.add_edge(n2, n1)
            if j > 0 and matrix[i][j] == matrix[i][j - 1]:
                n1, n2 = i * n_cols + j, i * n_cols + (j - 1)
                graph.add_edge(n1, n2)
                graph.add_edge(n2, n1)
    return graph


def get_num_countries_scratch(matrix: List[int], ncols: int) -> int:
    """ Given a matrix represented as a List with ncols
    find the the number of countries, without using a graph
    data structure"""
    visited = [False for _ in matrix]
    num_countries = 0
    for idx, elem in enumerate(matrix):
        if not visited[idx]:
            num_countries += 1
            # split
            visited[idx] = True
            queue = deque()
            queue.append(idx)
            while queue:
                current_idx = queue.popleft()
                for neighbor in _get_neighbors(matrix, ncols, current_idx):
                    if not visited[neighbor] and matrix[neighbor] == elem:
                        visited[neighbor] = True
                        queue.append(neighbor)
    return num_countries


def _get_neighbors_alt(matrix: List[int], ncols:int, idx:int) -> List[int]:
    row, col = idx//ncols, idx % ncols
    if row > 0:
        yield (row - 1)*ncols + col
    if col > 0:
        yield row * ncols + (col - 1)
    if row < len(matrix)/ncols - 1:
        yield (row + 1)*ncols + col
    if col < ncols - 1:
        yield row * ncols + (col + 1)


def _get_neighbors(matrix: List[int], ncols: int, idx: int) -> List[int]:
    if idx >= ncols:
        yield idx - ncols
    if (idx % ncols) != 0:
        yield idx - 1
    if idx < len(matrix) - ncols:
        yield idx + ncols
    if ((idx + 1) % ncols) != 0:
        yield idx + 1


if __name__ == "__main__":
    map1 = [
        [1, 2, 1, 2],
        [1, 1, 1, 3],
        [2, 3, 2, 2]
    ]
    map2 = [
        [32, 2, 1, 22],
        [32, 22, 22, 22],
        [22, 22, 2, 2]
    ]

    for my_map, res in [(map1, 7), (map2, 5)]:
        assert get_num_countries(my_map) == res

        my_map_as_list = [val for _list in my_map for val in _list]
        assert get_num_countries_scratch(my_map_as_list, 4) == res
