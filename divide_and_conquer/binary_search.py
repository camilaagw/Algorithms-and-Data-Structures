from typing import List


def binary_search(values: List[int], key: int) -> int:
    """Binary search algorithm

    :param values: ordered list of integers
    :param key: integer to find in values
    :return: Index in values where key is located at
    """

    if not values:
        return -1

    mid_point = len(values)//2

    if values[mid_point] < key:
        return binary_search(values[mid_point+1:], key)
    elif values[mid_point] > key:
        return binary_search(values[:mid_point], key)
    else:
        return mid_point


if __name__ == "__main__":

    values = [1, 5, 8, 12, 13]
    keys = [8, 1, 23, 1, 11]
    indices = [2, 0, -1, 0, -1]
    for key, idx in zip(keys, indices):
        assert binary_search(values, key) == idx
