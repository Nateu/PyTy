import random


def get_every_second_number(numbers: [int]) -> [int]:
    # loop = 0
    # result = []
    # for number in numbers:
    #     loop += 1
    #     if loop % 2 == 0:
    #         result.append(number)
    # return result
    return [number for index, number in enumerate(numbers) if index % 2 == 1]
    # return numbers[1::2]


def monkey_trouble(monkey_one: bool, monkey_two: bool) -> bool:
    return monkey_one == monkey_two


def has_L337(arr: [str]) -> bool:
    # string = ""
    # for char in arr:
    #     string += char
    # return "L337" in string
    return "L337" in "".join(arr)


def multiply_opposite_side(number: int) -> int:
    return (7 - number) ** 2


def throw_and_multiply() -> (int, int):
    my_number = random.randrange(1, 6)
    return my_number, multiply_opposite_side(my_number)
