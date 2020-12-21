"""Find if a string is a permutation of another string"""

from collections import Counter


def is_permutation(string1, string2):

    return Counter(string1) == Counter(string2)


def is_permutation_alt(string1, string2):
    letters_map = {}

    for char in string1:
        if char in letters_map:
            letters_map[char] += 1
        else:
            letters_map[char] = 1

    for char in string2:
        if char not in letters_map or letters_map[char] == 0:
            return False
        letters_map[char] -= 1

    for char in letters_map:
        if letters_map[char] != 0:
            return False

    return True


if __name__ == "__main__":

    for func in [is_permutation_alt, is_permutation]:
        assert func("camila", "amilac")
        assert not func("camila", "andrea")
