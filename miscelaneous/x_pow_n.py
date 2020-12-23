"""Compute x pow n in logarithmic time"""


def my_pow(x: float, n: int) -> float:

    def _pow(x, n):
        if n == 0:
            return 1
        if n % 2:
            return x * my_pow(x, n - 1)
        pow_n_half = my_pow(x, int(n / 2))
        return pow_n_half * pow_n_half

    if x == 0:
        return 0
    if n < 0:
        return 1/_pow(x, abs(n))
    return _pow(x, n)


if __name__ == "__main__":
    assert my_pow(3, 0) == 1
    assert my_pow(2, 5) == 32
    assert my_pow(5, 3) == 125
    assert my_pow(-2, 3) == -8
    assert my_pow(-2, 2) == 4
    assert my_pow(1234, 1) == 1234
    assert my_pow(2, -3) == 0.125
    assert my_pow(0, 10^28) == 0
