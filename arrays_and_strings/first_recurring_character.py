"""Find the first recurring character in a string"""


def first_recurring_char(string):
    chars_set = set()
    for char in string:
        if char in chars_set:
            return char
        chars_set.add(char)


if __name__ == "__main__":

    assert first_recurring_char('abc') is None
    assert first_recurring_char('abaca') == 'a'



