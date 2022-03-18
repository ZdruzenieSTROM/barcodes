#!/usr/bin/env python

from itertools import starmap
from operator import mul
from typing import Iterable


def digits(n: int) -> Iterable[int]:
    if not n:
        yield 0
        return

    while n:
        yield n % 10
        n //= 10


def stevkohash(n: int) -> int:
    WEIGHTS = (7, 3, 9, 1, 5, )

    return sum(starmap(mul, zip(digits(n), WEIGHTS))) % 10


def main() -> None:
    for line in iter(input, ""):
        try:
            n = int(line)

            print(stevkohash(n))
        except ValueError:
            print("Format Error")


if __name__ == "__main__":
    main()
