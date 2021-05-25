"""
Tom works in a video game park and sells to customers tokens to play. Find the minimum
number of tokens Tom can use to match the customer requests. He has tokens worth
100, 50, 25, 10, 5, 1. For example, for 126 Tom should give 3 tokens (100, 25, 1)

Check a more flexible version of the problem in ../recursion-and-dynamic-programming
"""

from typing import List

TOKENS = [100, 50, 25, 10, 5, 1]


def min_num_tokens(money: int, tokens_list: List[int] = TOKENS) -> int:
    tokens = 0
    for token in tokens_list:
        if money == 0:
            break
        num_tokens = money // token
        money -= num_tokens*token
        tokens += num_tokens

    return tokens


if __name__ == "__main__":

    assert min_num_tokens(126) == 3
    assert min_num_tokens(52) == 3

    #TODO: Raise exception for negative values
