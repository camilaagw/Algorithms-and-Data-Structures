"""
Implementation of the knapsack problem with and without replacement
"""

import numpy as np
from typing import List


def knapsack(total_capacity: int, item_values: List, item_sizes: List, replacement: bool = False) -> int:
    """Traditional knapsack problem (with and without replacement)

    :param total_capacity: Total capacity of the Knapsack
    :param item_values: List of item values ordered from lowest to highest one
    :param item_sizes: List of item sizes ordered according to item_values
    :param replacement: Whether to use replacement or not

    :return maximum value that fits on the knapsack
    """
    # Initialize array of items used
    items_used = []

    # Determine adjustment constant depending on replacement
    adjustment = int(not replacement)

    # Create initial matrix of values for capacities and items available
    values = np.zeros((total_capacity + 1, len(item_sizes) + 1))

    # Create initial matrix of item usage for capacities and items available
    usages = np.zeros((total_capacity + 1, len(item_sizes)))

    # Populate values matrix for every capacity, item, combination
    for items in range(len(item_values) + 1):
        idx = items - 1
        for capacity in range(total_capacity + 1):
            # No capacity or no items available
            if capacity == 0 or items == 0:
                pass
            # Check that current item fits the capacity
            elif item_sizes[idx] <= capacity:
                # Evaluate if the usage of the item maximizes the value
                new_value = item_values[idx] + values[capacity - item_sizes[idx], items - adjustment]
                values[capacity, items] = max(new_value, values[capacity, items - 1])
                # Report if item should be used or not
                if new_value == values[capacity, items]:
                    usages[capacity, idx] = 1
            else:
                values[capacity, items] = values[capacity, items - 1]

    # Determine which items were used
    idx_item = len(item_sizes) - 1
    capacity = total_capacity

    while idx_item >= 0:  # for i, e in reversed(list(enumerate(a))):
        if usages[capacity, idx_item] == 1:
            capacity = capacity - item_sizes[idx_item]
            items_used.append(item_sizes[idx_item])
            idx_item -= adjustment
        else:
            idx_item -= 1

    print(items_used)
    return values[-1, -1]


if __name__ == "__main__":
    assert knapsack(total_capacity=5,
                    item_values=[2],
                    item_sizes=[2]) == 2

    assert knapsack(total_capacity=28,
                    item_values=[2, 5, 10, 15],
                    item_sizes=[2, 5, 10, 15]) == 27

    assert knapsack(total_capacity=28,
                    item_values=[2, 5, 10, 15],
                    item_sizes=[2, 5, 10, 15][::-1]) == 30

    assert knapsack(total_capacity=5,
                    item_values=[2],
                    item_sizes=[2],
                    replacement=True) == 4

    assert knapsack(total_capacity=28,
                    item_values=[2, 5, 10, 15],
                    item_sizes=[2, 5, 10, 15],
                    replacement=True) == 28

    assert knapsack(total_capacity=28,
                    item_values=[2, 5, 10, 15],
                    item_sizes=[2, 5, 10, 15][::-1],
                    replacement=True) == 210
