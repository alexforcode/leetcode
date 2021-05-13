"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).

Return the number that I picked.

Constraints:
    1 <= n <= 2**31 - 1
    1 <= pick <= n
"""


def guess(num: int, pick: int):
    if num == pick:
        return 0
    elif num < pick:
        return 1
    elif num > pick:
        return -1


def guess_number(n: int, pick: int) -> int:
    start: int = 1
    end: int = n

    while start <= end:
        mid: int = (start + end) // 2
        guess_try: int = guess(mid, pick)

        if guess_try == 0:
            return mid
        elif guess_try == -1:
            end = mid - 1
        elif guess_try == 1:
            start = mid + 1


if __name__ == '__main__':
    assert guess_number(10, 6) == 6
    assert guess_number(1, 1) == 1
    assert guess_number(2, 1) == 1
    assert guess_number(2, 2) == 2
