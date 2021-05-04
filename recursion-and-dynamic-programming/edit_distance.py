"""Calculates edit distance using dynamic programming"""

import numpy as np


def get_edit_distance(string1: str, string2: str) -> int:
    """Levenshtein distance calculation
    Minimun number of insertions, deletions or replacements between two strings
    """
    len_s1 = len(string1)
    len_s2 = len(string2)
    distances = np.zeros((len_s1 + 1, len_s2 + 1))

    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            # Comparisons to an empty string
            if i == 0 or j == 0:
                distances[i, j] = i or j
            # Comparison with matching letters
            elif string1[i - 1] == string2[j - 1]:
                distances[i, j] = distances[i - 1, j - 1]
            # Non matching letters
            else:
                distances[i, j] = 1 + min(distances[i - 1, j - 1], distances[i, j - 1], distances[i - 1, j])

    return distances[i, j]


if __name__ == "__main__":
    assert get_edit_distance("wpaanamericana", "pnameticanaa") == 5
    assert get_edit_distance("geek", "gesek") == 1
    assert get_edit_distance("sunday", "saturday") == 3
