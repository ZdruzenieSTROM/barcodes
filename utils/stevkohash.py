#!/usr/bin/env python

from itertools import starmap
from operator import mul
from sys import stdin
from typing import Iterable


def digits(n: int) -> Iterable[int]:
    if not n:
        yield 0
        return

    while n:
        yield n % 10
        n //= 10


def stevkohash(n: int) -> int:
    WEIGHTS = [5, 1, 9, 3, 7]

    return sum(starmap(mul, zip(digits(n), reversed(WEIGHTS)))) % 10


def main() -> None:
    for line in stdin:
        try:
            print(stevkohash(int(line)))
        except ValueError:
            pass


if __name__ == "__main__":
    main()
