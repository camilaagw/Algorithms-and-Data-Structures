"""Find if a string is a permutation of another string"""

from collections import Counter


def is_permutation(string1: str, string2: str) -> bool:
    return Counter(string1) == Counter(string2)


def is_permutation_alt(string1: str, string2: str) -> bool:
    """Using just one counter (less space)"""
    letters_map = Counter(string1)

    for char in string2:
        if char not in letters_map or letters_map[char] == 0:
            return False
        letters_map[char] -= 1

    return sum(letters_map.values()) == 0


if __name__ == "__main__":

    for func in [is_permutation_alt, is_permutation]:
        assert func("camila", "amilac")
        assert not func("camila", "andrea")
