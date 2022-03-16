#!/usr/bin/env python

from argparse import ArgumentParser
from os import makedirs
from typing import Iterable


def starting_line(line: str) -> bool:
    return r"\begin{zadanie}" in line


def ending_line(line: str) -> bool:
    return r"\end{zadanie}" in line


def dump_problem(content: Iterable[str], number: int, outdir: str) -> None:
    with open(f"{ outdir }/zadanie{ number }.tex", "w") as target:
        target.writelines(content)


def partition_single_file(path: str, last_number: int, outdir: str) -> int:
    with open(path, "r") as file:
        content = []
        number = last_number

        for line in file:
            if starting_line(line):
                content.clear()
                number += 1

            content.append(line)

            if ending_line(line):
                dump_problem(content, number, outdir)

        return number


def partion_problems(sources: Iterable[str], outdir: str) -> None:
    last_number = 0

    makedirs(outdir, exist_ok=True)

    for path in sources:
        last_number = partition_single_file(path, last_number, outdir)


def main() -> None:
    parser = ArgumentParser()

    parser.add_argument("files", nargs="+")
    parser.add_argument("--outdir", "-o", required=True)

    config = parser.parse_args()

    partion_problems(config.files, config.outdir)


if __name__ == "__main__":
    main()
