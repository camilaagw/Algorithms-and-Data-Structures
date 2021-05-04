"""Imagine a robot sitting on the upper left corner of grid with r rows
and c columns. The robot can only move in two directions, right and down, but
certain cells are "off limits" such that the robot cannot step on them.
Design an algo to find a path for the robot from the top-left to the bottom right"""

from typing import List


def solution(grid: List[List[int]]) -> List[List[bool]]:
    rows = len(grid)
    cols = len(grid[0])
    reach_grid = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i == 0 and j == 0:
                    reach_grid[i][j] = 1
                elif i == 0:
                    reach_grid[i][j] = reach_grid[i][j - 1]
                elif j == 0:
                    reach_grid[i][j] = reach_grid[i - 1][j]
                else:
                    reach_grid[i][j] = reach_grid[i][j - 1] or reach_grid[i - 1][j]

    print(reach_grid)
    j = cols - 1
    i = rows - 1
    if reach_grid[i][j]:
        movements = []
        while i != 0 or j != 0:
            if i > 0 and reach_grid[i-1][j]:
                movements.append('down')
                i -= 1
            else:
                movements.append('right')
                j -= 1
        movements.reverse()
        print(movements)
        return movements


if __name__ == "__main__":
    mov = solution(
        [
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 1, 1]
        ]
    )

