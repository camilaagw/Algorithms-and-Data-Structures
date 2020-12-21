from typing import List


def fractional_knapsack(weight: int, values: List[int], weights: List[int]):
    """Fractional knapsack problem

    :param weight: Knapsack total weight
    :param values: Values of items sorted from highest to lower
    :param weights: Weights of items sorted according to values (from highest to lower)
    :return: Maximum value
    """
    total_value = 0

    for v, w in zip(values, weights):
        if weight == 0:
            break

        amount = min(w, weight)
        total_value += v * amount/w
        weight -= amount

    return total_value


if __name__ == "__main__":

    assert fractional_knapsack(10, [500], [30]) == 500/3
    assert fractional_knapsack(50, [120, 100, 60], [30, 50, 20])


