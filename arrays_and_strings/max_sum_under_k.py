"""
Given an array of integers and a value K find a contiguous subsequence having maximum sum under K.
Return the maximum Sum.
"""


def max_sum_capped(array, limit):
    start = 0
    max_sum = 0
    current_sum = 0
    for idx, elem in enumerate(array):

        if elem < 0:
            start += 1
        else:
            current_sum += elem

        while current_sum > limit:
            current_sum -= array[start]
            start += 1

        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    assert max_sum_capped([1, 2, 3, 4, 5, 6, 7, 16], 15) == 15
    assert max_sum_capped([1, 2, 3, 12, 3], 10) == 6
    assert max_sum_capped([20, 20, 20], 2) == 0
    assert max_sum_capped([-1, -2, 4, 4, 5, 5, 7, 16], 15) == 14
