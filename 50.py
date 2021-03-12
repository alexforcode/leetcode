"""
Implement pow(x, n), which calculates x raised to the power n (i.e. x**n).

Constraints:
    -100.0 < x < 100.0
    -2**31 <= n <= 2**31-1
    -10**4 <= xn <= 10**4
"""


def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        return 1 / my_pow(x, -n)

    temp: float = my_pow(x, int(n/2))
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp


if __name__ == '__main__':
    print(my_pow(2.0, 10))  # 1024.00
    print(my_pow(2.1, 3))   # 9.26100
    print(my_pow(2.0, -2))  # 0.25000
