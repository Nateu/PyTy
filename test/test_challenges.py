from pascal import (
    get_every_second_number,
    monkey_trouble,
    has_L337,
    multiply_opposite_side,
)


def test_get_second_numbers():
    numbers = [1, 2, 3, 4]
    assert get_every_second_number(numbers) == [2, 4]


def test_monkey_trouble_first_one_smiles():
    a_smile = True
    b_smile = False
    assert monkey_trouble(a_smile, b_smile) is False


def test_monkey_trouble_second_one_smiles():
    a_smile = False
    b_smile = True
    assert monkey_trouble(a_smile, b_smile) is False


def test_monkey_trouble_none_smiles():
    a_smile = False
    b_smile = False
    assert monkey_trouble(a_smile, b_smile) is True


def test_monkey_trouble_both_smile():
    a_smile = True
    b_smile = True
    assert monkey_trouble(a_smile, b_smile) is True


def test_has_L337_not_found():
    arr = ["alkda", "asd33cf7ldj", "lregh"]
    assert has_L337(arr) is False


def test_has_L337_found():
    arr = [
        "a",
        "l",
        "k",
        "d",
        "a",
        "a",
        "s",
        "k",
        "L",
        "3",
        "3",
        "7",
        "l",
        "d",
        "j",
        "l",
        "r",
        "e",
        "g",
        "h",
    ]
    assert has_L337(arr) is True


def test_multiply_opposite_side_1():
    assert multiply_opposite_side(1) == 36


def test_multiply_opposite_side_2():
    assert multiply_opposite_side(2) == 25


def test_multiply_opposite_side_3():
    assert multiply_opposite_side(3) == 16


def test_multiply_opposite_side_4():
    assert multiply_opposite_side(4) == 9


def test_multiply_opposite_side_5():
    assert multiply_opposite_side(5) == 4


def test_multiply_opposite_side_6():
    assert multiply_opposite_side(6) == 1
