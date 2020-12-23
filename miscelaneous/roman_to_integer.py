"""Write a python function to convert a roman number to an integer"""


def roman_to_integer(roman: str) -> int:
    mapping = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
        "": 0
    }

    prev_val = 0
    integer = 0

    for sym in roman:
        current_val = mapping[sym]
        integer += current_val
        if current_val > prev_val:
            integer -= 2*prev_val
        prev_val = current_val

    return integer


if __name__ == "__main__":
    assert roman_to_integer("MI") == 1001
    assert roman_to_integer("MMMM") == 4000
    assert roman_to_integer("") == 0
    assert roman_to_integer("IV") == 4
    assert roman_to_integer("XXXVI") == 36
    assert roman_to_integer("MMXII") == 2012
    assert roman_to_integer("MCMXCVI") == 1996
