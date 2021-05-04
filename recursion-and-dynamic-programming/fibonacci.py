import numpy as np


def fibonacci(n: int) -> int:
    """Get the nth Fibonacci number"""
    fib_sequence = np.zeros(n + 1)
    fib_sequence[1] = 1
    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

    return fib_sequence[i]


def fibonacci_last_digit(n: int) -> int:
    """Efficient implementation to get the last digit of the nth Fibonacci number"""
    fib_sequence = np.zeros(n + 1)
    fib_sequence[1] = 1
    for i in range(2, n + 1):
        fib_sequence[i] = (fib_sequence[i - 1] + fib_sequence[i - 2]) % 10

    return fib_sequence[i]


def fibonacci_modulo(n: int, m: int) -> int:
    """Compute Fibonacci(n) modulo m, where n may be really huge: up to 10^18.
    Note that for any integer 𝑚 ≥ 2, the sequence  Fibonacci(n) modulo m is periodic.
    The period always starts with 01 and is known as Pisano period.
    """
    fib_mod_seq = [0, 1, 1]
    i = 3

    while fib_mod_seq[-2:] != [0, 1]:
        fib_mod_seq.append((fib_mod_seq[i - 1] + fib_mod_seq[i - 2]) % m)
        i += 1

    period_len = len(fib_mod_seq) - 2
    return fib_mod_seq[n % period_len]


def fibonacci_last_digit_sum(n: int) -> int:
    """Find the last digit of a sum of the first 𝑛 Fibonacci numbers."""
    fib_sequence = np.zeros(n + 1)
    fib_sequence[1] = 1
    for i in range(2, n + 1):
        fib_sequence[i] = (fib_sequence[i - 1] + fib_sequence[i - 2]) % 10

    return sum(fib_sequence) % 10


def fibonacci_last_digit_partial_sum(start: int, n: int, ) -> int:
    """Find the last digit of a partial sum of Fibonacci numbers: 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛."""
    fib_sequence = np.zeros(n + 1)
    fib_sequence[1] = 1
    for i in range(2, n + 1):
        fib_sequence[i] = (fib_sequence[i - 1] + fib_sequence[i - 2]) % 10

    return sum(fib_sequence[start:]) % 10


def fibonacci_last_digit_sum_squares(n: int) -> int:
    """Compute the last digit of 𝐹0^2 + 𝐹1^2 + · · · + 𝐹n^2"""
    area = fibonacci_modulo(n, 10) * (fibonacci_modulo(n, 10) + fibonacci_modulo(n - 1, 10))
    return area % 10


if __name__ == "__main__":
    assert fibonacci(10) == 55

    assert fibonacci_last_digit(331) == 9
    assert fibonacci_last_digit(327305) == 5

    assert fibonacci_modulo(2015, 3) == 1
    assert fibonacci_modulo(239, 1000) == 161
    assert fibonacci_modulo(2816213588, 239) == 151

    assert fibonacci_last_digit_sum(3) == 4
    assert fibonacci_last_digit_sum(100) == 5

    assert fibonacci_last_digit_partial_sum(3, 7) == 1
    assert fibonacci_last_digit_partial_sum(10, 10) == 5
    assert fibonacci_last_digit_partial_sum(10, 200) == 2

    assert fibonacci_last_digit_sum_squares(7) == 3
    assert fibonacci_last_digit_sum_squares(73) == 1
    assert fibonacci_last_digit_sum_squares(1234567890) == 0
