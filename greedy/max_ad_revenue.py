"""Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is
the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗)
such that the sum of their products is maximized."""

from typing import List


def max_revenue(profits: List[int], click_rates: List[int]):
    profits.sort()
    click_rates.sort()

    return sum([p*c for p, c in zip(profits, click_rates)])


if __name__ == "__main__":

    assert max_revenue([34], [42]) == 34*42
    assert max_revenue([1,3,-5], [-2,4,1]) == 23