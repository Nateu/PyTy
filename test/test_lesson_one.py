from pascal import get_pascal, get_pascal_one_line


def test_resolve_name_by_index():
    assert get_pascal() == 5


def test_get_pascal_one_line():
    assert get_pascal_one_line() == 5
