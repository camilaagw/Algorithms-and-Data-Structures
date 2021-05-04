"""Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a re-arrangement of letters. You can ignore spaces"""


def is_palindrome(string: str) -> bool:
    seen_chars = set()
    for char in string:
        if char != ' ':
            if char in seen_chars:
                seen_chars.remove(char)
            else:
                seen_chars.add(char)
    return len(seen_chars) <= 1


if __name__ == "__main__":
    assert is_palindrome("taco act")
    assert is_palindrome("")
    assert is_palindrome("holidays are here")