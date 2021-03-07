from graph_base import Graph
from typing import List


def map_to_graph(matrix: List[List[int]]) -> Graph:
    n_rows, n_cols = len(matrix), len(matrix[0])
    size = 0
    edges = []
    node_number = {}
    for i in range(n_rows):
        for j in range(n_cols):
            elem = matrix[i][j]
            if elem == 1:
                size += 1
                node_number[(i, j)] = size - 1
                if i > 0:
                    if matrix[i - 1][j] == 1:
                        edges.append(
                            (node_number[(i, j)], node_number[(i-1, j)])
                        )
                if j > 0:
                    if matrix[i][j - 1] == 1:
                        edges.append(
                            (node_number[(i, j)], node_number[(i, j-1)])
                        )

    print(matrix)
    return Graph.non_directed_from_edges(size, edges)

# TODO: Repeat islands problem without a graph stucture


if __name__ == "__main__":
    my_map = [
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 1]
    ]
    print(map_to_graph(my_map))
