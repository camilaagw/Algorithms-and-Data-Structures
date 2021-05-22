"""Given an array of positive numbers, find the maximum sum of a subsequence with the constraint
that no 2 numbers in the sequence should be adjacent in the array."""

from typing import List


def max_non_adjacent_sum(values: List[int]) -> int:
    if not values:
        return 0
    if len(values) == 1:
        return values[0]

    return max(
        max_non_adjacent_sum(values[1:]),
        values[0] + max_non_adjacent_sum(values[2:])
    )


def max_non_adjacent_sum_alt(throughput):
    excl, incl = 0, 0
    for i in throughput:
        new_excl = excl if excl > incl else incl
        incl = excl + i
        excl = new_excl
    return excl if excl > incl else incl


if __name__ == "__main__":
    assert max_non_adjacent_sum([3, 2, 7, 10]) == 13
    assert max_non_adjacent_sum([3, 2, 5, 10, 7]) == 15
    assert max_non_adjacent_sum([1, 3, 1, 2]) == 5
