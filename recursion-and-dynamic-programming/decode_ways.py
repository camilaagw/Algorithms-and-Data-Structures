"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:
Input: s = "1"
Output: 1

Constraints
1 <= s.length <= 100
s contains only digits and may contain leading zero(s)
"""


def get_num_decoding_ways(string: str) -> int:
    """Base implementation"""

    if string.startswith('0'):
        return 0
    if string == '':
        return 1
    if len(string) >= 2 and int(string[:2]) <= 26:
        return get_num_decoding_ways(string[1:]) + get_num_decoding_ways(string[2:])

    return get_num_decoding_ways(string[1:])


def get_num_decoding_ways_alt(my_string: str) -> int:
    """Implementation using dynamic programming"""
    num_ways = {}

    def helper(string: str, index: int) -> int:

        n = len(string)
        if index == n:
            return 1
        if string[index] == '0':
            return 0

        if index in num_ways:
            return num_ways[index]

        result = helper(string, index + 1)
        if n - index >= 2 and int(string[index:index + 2]) <= 26:
            result += helper(string, index + 2)
        num_ways[index] = result

        return result

    return helper(my_string, index=0)


if __name__ == "__main__":

    for string, result in [('226', 3), ('12', 2), ('101', 1), ('100', 0), ('01', 0), ('12345', 3)]:
        assert get_num_decoding_ways(string) == result
        assert get_num_decoding_ways_alt(string) == result
