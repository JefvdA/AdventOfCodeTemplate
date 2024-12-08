#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest
from timeit import timeit


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    return 0


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("", 0),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        ex_time = timeit(lambda: print(compute(f.read())), number=1)
    print(f"Execution time: {ex_time:.3f} seconds")


if __name__ == "__main__":
    main()