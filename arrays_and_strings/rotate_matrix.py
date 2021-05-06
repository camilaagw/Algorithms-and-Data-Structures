"""Rotate a N by N matrix by 90 degrees"""

from typing import List, Tuple


def rotate(matrix: List[List[int]]):
    n = len(matrix)

    if n % 2 == 0:
        max_rows = max_cols = n//2
    else:
        max_rows = n//2
        max_cols = n//2 + 1

    for i in range(max_rows):
        for j in range(max_cols):
            curr_i, curr_j = i, j
            temp = matrix[i][j]
            for _ in range(4):
                curr_i, curr_j = next_position(n, curr_i, curr_j)
                temp, matrix[curr_i][curr_j] = matrix[curr_i][curr_j], temp


def next_position(n: int, i: int, j: int) -> Tuple[int, int]:
    """Returns the position to which the element in i,j goes to
     when rotated 90 degrees"""
    return n - 1 - j, i


if __name__ == "__main__":
    matrix = [
        [1, 2],
        [3, 4]
    ]
    rotate(matrix)
    assert matrix == [
        [2, 4],
        [1, 3]
    ]

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate(matrix)
    assert matrix == [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    rotate(matrix)
    assert matrix == [
        [4, 8, 12, 16],
        [3, 7, 11, 15],
        [2, 6, 10, 14],
        [1, 5, 9, 13]
    ]



