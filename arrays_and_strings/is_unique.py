"""Are all characters in a string unique?"""


def main(my_string: str) -> bool:

    my_set = set()
    for char in my_string:
        if char not in my_set:
            my_set.add(char)
        else:
            return False

    return True


if __name__ == "__main__":
    assert not main("aasssasfsdfdfdf")
    assert main("abcdegf")
