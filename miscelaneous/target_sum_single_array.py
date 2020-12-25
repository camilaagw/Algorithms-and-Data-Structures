"""Write a function to find a pair of elements (indices of the two numbers)
from a given array whose sum equals a specific target number"""

from typing import List


def find_pair(values: List[int], target: int) -> List[int]:
    """Solution using a sorted list"""
    down_idx = len(values) - 1
    up_idx = 0

    while (down_idx >= 0) and (up_idx <= len(values) - 1) and (down_idx != up_idx):

        temp_sum = values[down_idx] + values[up_idx]
        if temp_sum == target:
            return [up_idx, down_idx]
        if temp_sum < target:
            up_idx += 1
        else:
            down_idx -= 1

    return []


def find_pair_alt(values: List[int], target: int) -> List[int]:
    """Alternative solution that does not need a sorted list"""
    values_dict = {val: idx for idx, val in enumerate(values)}
    
    for idx, val in enumerate(values):
        if target-val in values_dict:
            return [idx, values_dict[target-val]]
    
    return []
            

if __name__ == "__main__":
    my_array = [-100, 10, 20, 30, 40, 50, 70, 80]
    for func in [find_pair, find_pair_alt]:
        assert func(my_array, 50) == [1, 4]
        assert func(my_array, 500) == []
        assert func(my_array, -1) == []
        assert func(my_array, -90) == [0, 1]
        assert func(my_array, -30) == [0, 6]
        assert func(my_array, 150) == [6, 7]

    my_array = [20, 12, -10, 15]
    assert find_pair_alt(my_array, 27) == [1, 3]
    assert find_pair_alt(my_array, 5) == [2, 3]
