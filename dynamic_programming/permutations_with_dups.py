"""Find all the permutations of a string that might contain duplicates"""
from typing import List
from collections import Counter


def get_permutations(string: str) -> List[str]:
    """Recursive version"""
    counter_ = Counter(string)
    def helper(counter):
        if sum(counter.values()) == 0:
            return ['']
        perms = []
        for key in counter:
            if counter[key] > 0:
                copy_counter = counter.copy()
                copy_counter[key] -= 1
                for perm in helper(copy_counter):
                    perms.append(key+perm)
        return perms

    return helper(counter_)


if __name__ == "__main__":
    assert get_permutations('00011') == ['00011', '00101', '00110', '01001', '01010', '01100', '10001', '10010', '10100', '11000']
    assert get_permutations('abb') == ['abb', 'bab', 'bba']
    assert get_permutations('aaaaaaaaa') == ['aaaaaaaaa']

