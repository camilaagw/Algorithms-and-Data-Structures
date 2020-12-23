"""Write a function to convert positive integers to roman numbers"""


def integer_to_roman(integer: int) -> str:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    sym = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman = ''
    i = 0
    while integer > 0:
        for _ in range(integer//val[i]):
            roman += sym[i]
            integer -= val[i]
        i += 1

    return roman


if __name__ == "__main__":

    assert integer_to_roman(1001) == "MI"
    assert integer_to_roman(4000) == "MMMM"
    assert integer_to_roman(0) == ''
    assert integer_to_roman(36) == 'XXXVI'
    assert integer_to_roman(2012) == 'MMXII'
    assert integer_to_roman(1996) == 'MCMXCVI'