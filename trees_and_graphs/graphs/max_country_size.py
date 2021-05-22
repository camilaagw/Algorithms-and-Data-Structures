""" Given a matrix represented as a List with ncols
find the size of the largest country, without using a graph
data structure"""
from typing import List, Tuple
from collections import deque


def max_country_size_v1(matrix: List[List[int]]) -> int:
    """DFS recursive-approach: Careful with stack-overflow"""
    visited = set()
    rows, cols = len(matrix), len(matrix[0])

    def traverse(idx: Tuple[int, int], size) -> int:
        if idx not in visited:
            visited.add(idx)
            current_elem = matrix[idx[0]][idx[1]]
            size += 1
            for next_idx in _get_neighbors(idx, rows, cols):
                nxt_i, nxt_j = next_idx
                if next_idx not in visited and current_elem == matrix[nxt_i][nxt_j]:
                    size = traverse(next_idx, size)
        return size

    max_size = 0
    for i in range(rows):
        for j in range(cols):
            max_size = max(traverse(idx=(i, j), size=0), max_size)

    return max_size


def max_country_size_v2(matrix: List[List[int]]) -> int:
    """BFS iterative-approach"""
    visited = set()
    max_size = 0
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            size = 0
            if (i, j) not in visited:
                visited.add((i, j))
                queue = deque([(i, j)])
                while queue:
                    current_index = queue.popleft()
                    current_elem = matrix[current_index[0]][current_index[1]]
                    size += 1
                    for idx in _get_neighbors(current_index, rows, cols):
                        if idx not in visited and current_elem == matrix[idx[0]][idx[1]]:
                            visited.add(idx)
                            queue.append(idx)
            max_size = max(size, max_size)
    return max_size


def _get_neighbors(index: Tuple[int, int], rows: int, cols: int):
    i, j = index
    if i > 0:
        yield i - 1, j
    if j > 0:
        yield i, j - 1
    if i + 1 < rows:
        yield i + 1, j
    if j + 1 < cols:
        yield i, j + 1


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

    for func in [max_country_size_v1, max_country_size_v2]:
        assert func(map1) == 5
        assert func(map2) == 6
