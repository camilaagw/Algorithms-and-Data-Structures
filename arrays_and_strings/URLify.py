"""Write a method to replace all spaces in a string with '%20'. You may asume that
the string has sufficient space at the end to hold the additional characters, and that
you are only given the true length of the string
"""


def urlify(input_string: str) -> str:
    string = list(input_string)
    i = j = len(string) - 1

    # Place j in the rightmost char different from space
    while string[j] == ' ':
        j -= 1

    # Replace spaces
    while i > j:
        if string[j] == ' ':
            string[j: i+1] = ['%', '2', '0']
            i -= 3
        else:
            string[i] = string[j]
            i -= 1
        j -= 1

    return ''.join(string)


if __name__ == "__main__":
    assert urlify("hello world  ") == "hello%20world"
