"""Edit distance of 1 or less:
Given two strings, write a function to check if they are one edit or zero away"""


def max_one_edit_away(string1: str, string2: str) -> bool:
    len1, len2 = len(string1), len(string2)
    if abs(len1 - len2) > 1:
        return False

    diff = 0
    # Case in which both strings have the same length
    if len1 == len2:
        for char1, char2 in zip(string1, string2):
            if char1 != char2:
                diff += 1
    # Case in which both strings have different length
    else:
        len_ = len1 if len1 < len2 else len2
        small = string1 if len1 < len2 else string2
        large = string2 if len1 < len2 else string1

        i = j = 0
        while i < len_:
            if small[i] == large[j]:
                i += 1
                j += 1
            elif diff == 0:
                diff += 1
                j += 1
            else:
                return False

    return diff <= 1


if __name__ == "__main__":
    assert max_one_edit_away("home", "hme")
    assert max_one_edit_away("home", "ome")
    assert max_one_edit_away("home", "hme")
    assert max_one_edit_away("home", "hoe")
    assert max_one_edit_away("home", "hom")
    assert max_one_edit_away("home", "home")
    assert not max_one_edit_away("home", "hem")
    assert not max_one_edit_away("home", "ho")


