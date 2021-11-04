import random
from typing import List


def get_every_second_number(numbers: List[int]) -> List[int]:
    return [number for index, number in enumerate(numbers) if index % 2 == 1]


def monkey_trouble(monkey_one: bool, monkey_two: bool) -> bool:
    return monkey_one == monkey_two


def has_L337(arr: [str]) -> bool:
    return "L337" in "".join(arr)


def multiply_opposite_side(number: int) -> int:
    return (7 - number) ** 2


def throw_and_multiply() -> (int, int):
    my_number = random.randrange(1, 6)
    return my_number, multiply_opposite_side(my_number)
