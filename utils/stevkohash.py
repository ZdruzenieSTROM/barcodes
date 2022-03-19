#!/usr/bin/env python

from itertools import starmap
from operator import mul
from typing import Iterable


def digits(number: int) -> Iterable[int]:
    if not number:
        yield 0
        return

    remainder = number

    while remainder:
        yield remainder % 10
        remainder //= 10


def stevkohash(n: int) -> int:
    WEIGHTS = (7, 3, 9, 1, 5, )

    return sum(starmap(mul, zip(digits(n), WEIGHTS))) % 10


def main() -> None:
    for line in iter(input, ""):
        try:
            number = int(line)

            print(stevkohash(number))

        except ValueError:
            print("Format Error")


if __name__ == "__main__":
    main()
