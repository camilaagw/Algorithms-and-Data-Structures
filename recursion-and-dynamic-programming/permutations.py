"""Find all the permutations of a string"""
from typing import Set


def get_permutations(input_: str) -> Set[str]:
    """Iterative implementation"""
    if len(input_) == 0:
        return {}
    permutations = {''}
    for elem in input_:
        new_permutations = set()
        for str_ in permutations:
            for i in range(len(str_)+1):
                new_permutations.add(str_[0:i]+elem+str_[i:])
        permutations = new_permutations

    return permutations


def get_permutations_v2(input_: str) -> Set[str]:
    """Recursive implementation"""
    if len(input_) == 0:
        return {}
    if len(input_) == 1:
        return {input_}
    new_permutations = set()
    for p in get_permutations_v2(input_[1:]):
        for i in range(len(p) + 1):
            new_permutations.add(p[0:i] + input_[0] + p[i:])
    return new_permutations


if __name__ == "__main__":
    assert get_permutations_v2('abc') == {'acb', 'bca', 'abc', 'bac', 'cab', 'cba'}
    assert get_permutations_v2('aabc') == {'cbaa', 'aabc', 'baac', 'bcaa', 'caba', 'acba',
                                           'abac', 'acab', 'baca', 'abca', 'caab', 'aacb'}




