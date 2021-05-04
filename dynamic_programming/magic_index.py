"""A magic index in an array A[0,...,n-1] is defined to be an index such that
A[i]=i. Given a **sorted** array of distinct integers, write a method to find a
magic index, if one exists, in an Array A"""

from typing import List


def get_magic_index_naive(array: List[int]) -> int:
    for i, elem in enumerate(array):
        if i == elem:
            return i
    return -1


def get_magic_index(array: List[int]) -> int:
    """Optimized version"""
    def helper(start: int, end: int) -> int:
        mid_point = (end - start)//2 + start
        if array[mid_point] == mid_point:
            return mid_point
        if array[mid_point] < mid_point and array[end] >= end:
            return helper(mid_point + 1, end)
        if array[mid_point] > mid_point and array[start] <= start:
            return helper(start, mid_point-1)
        return -1
    return helper(0, len(array)-1)


def get_magic_index_v2(array: List[int]) -> int:
    """Optimized version allowing for equal indices"""
    def helper(start: int, end: int) -> int:
        if end < start:
            return -1
        mid_point = (end - start)//2 + start
        if array[mid_point] == mid_point:
            return mid_point
        if array[mid_point] < mid_point:
            return max(
                helper(mid_point + 1, end),
                helper(start, min(mid_point - 1, array[mid_point]))
            )
        if array[mid_point] > mid_point:
            return max(
                helper(start, mid_point-1),
                helper(max(mid_point + 1, array[mid_point]), end),
            )
    return helper(0, len(array)-1)


if __name__ == "__main__":

    for func in [get_magic_index, get_magic_index_naive, get_magic_index_v2]:
        assert func([-100, -2, -1, 3, 100]) == 3
        assert func([-100, -99, -18, -3, 1]) == -1
        assert func([100, 101, 102, 103, 104]) == -1
        assert func([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]) == 7

    assert get_magic_index_v2([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]) == 7
    assert get_magic_index_v2([-40, -20, 2, 2, 2, 3, 5, 8, 9, 12, 13]) == 2
    assert get_magic_index_v2([-40, -20, -1, 1, 2, 7, 8, 8, 8, 12, 13]) == 8

