"""
Given two arrays, find the pair(s) of numbers whose sum is the closest one to a specific target.
Within a pair, each must come from a different array.
For example, given the arrays [-1, 3, 8, 2, 9, 5] and [4, 1, 2, 10, 5, 20], and the target 24
the best we could do is to have the pairs (20, 3) and (20, 5)
Assume none of the arrays are empty and there are no repeated numbers in the arrays
"""
from typing import List


def closest_sum(A: List[int], B: List[int], target: int):
    A.sort()
    B.sort()

    a = 0
    b = len(B) - 1
    best_distance = float('inf')
    best_pairs = []
    while a < len(A) and b >= 0:
        diff = A[a] + B[b] - target
        
        if best_distance == abs(diff):
            best_pairs.append((A[a], B[b]))
        elif best_distance > abs(diff):
            best_distance = abs(diff)
            best_pairs = [(A[a], B[b])]

        if diff > 0:
            b -= 1
        else:
            a += 1

    return best_pairs


if __name__ == '__main__':
    assert closest_sum([-1, 3, 8, 2, 9, 5], [4, 1, 2, 10, 5, 20], 24) == [(3, 20), (5, 20)]
    assert closest_sum([1, 3, 8, 2, 9, 5], [11, 1, 2], 12) == [(1, 11)]
    assert closest_sum([4, 6], [4, 6], 10) == [(4, 6), (6, 4)] 
    assert closest_sum([4, 6], [4, 6], 11) == [(4, 6), (6, 6), (6, 4)]





