"""Are all characters in a string unique?"""


def is_unique(my_string: str) -> bool:
    """Using a hash-set"""
    my_set = set()
    for char in my_string:
        if char in my_set:
            return False
        my_set.add(char)
    return True


def is_unique_v1(my_string: str) -> bool:
    """Using a bit vector :)"""
    checker = 0
    for char in my_string:
        position = ord(char) - 97
        if (checker & (1 << position)) > 0:
            return False
        checker |= (1 << position)
    return True


if __name__ == "__main__":

    for func in [is_unique, is_unique_v1]:
        assert not func("aasssasfsdfdfdf")
        assert func("abcdegf")
