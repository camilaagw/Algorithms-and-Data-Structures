"""
Tom works in a video game park and sells to customers tokens to play. Find the minimum
number of tokens Tom can use to match the customer requests. He has tokens worth
100, 80, 25, 10, 8, 1. For example, for 126 Tom should give 3 tokens (100, 25, 1),
and for 160 he should give 2 tokens (80, 80).
"""

TOKENS = [100, 80, 25, 10, 8, 1]


def min_num_tokens(total_amount):
    """Recursive solution"""
    def helper(amount, idx):
        if amount == 0:
            return 0
        token_val = TOKENS[idx]
        num_tokens = amount // token_val
        if idx == len(TOKENS) - 1:
            return num_tokens
        return min(
            # Use the token
            num_tokens + helper(amount - num_tokens * token_val, idx + 1),
            # Don't use the token
            helper(amount, idx + 1)
        )
    return helper(total_amount, 0)


def min_num_tokens_v2(amount):
    """Dynamic programming solution"""
    memo = [0] + [float('inf')] * amount
    for token in TOKENS:
        for j in range(token, amount + 1):
            # memo[j - token] + 1: use the token
            # memo[j] don't use the token
           memo[j] = min(memo[j - token] + 1, memo[j])
    return memo[-1]


if __name__ == "__main__":
    for func in [min_num_tokens, min_num_tokens_v2]:
        assert func(126) == 3, func(126)
        assert func(160) == 2