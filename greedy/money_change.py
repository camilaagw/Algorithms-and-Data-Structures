"""
Elementary greedy algorithm used by cashiers all over
the world millions of times per day.
"""

from typing import List


def money_change(m: int) -> int:
    """ Find the minimum number of coins needed to change the input value
    (an integer) into coins with denominations 1, 5, and 10

    :param m: Value to change for coins
    :return: minimum number of coins with denominations 1, 5, 10 that changes 𝑚
    """
    coins = [10, 5, 1]
    return convert_to_coins(m, coins)


def convert_to_coins(m: int, coins: List) -> int:
    if m == 0:
        return 0

    if coins[0] == 1:
        return m

    if coins[0] <= m:
        return min(m // coins[0] + convert_to_coins(m % coins[0], coins), convert_to_coins(m, coins[1:]))
    else:
        return convert_to_coins(m, coins[1:])


def money_change_simple(m: int) -> int:
    num_coins = 0

    for coin in [10, 5, 1]:
        if m == 0:
            return num_coins

        if coin <= m:
            num_coins += m // coin
            m = m % coin


def money_change_simpler(m: int) -> int:  # Probably the best solution

    num_coins = 0
    for coin in [10, 5, 1]:
        num_coins += m // coin
        m = m % coin

    return num_coins


if __name__ == "__main__":
    assert money_change(4) == 4
    assert money_change(5) == 1
    assert money_change(101) == 11
    assert money_change(28) == 6
