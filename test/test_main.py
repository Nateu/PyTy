from unittest import TestCase
from pascal import get_pascal, get_pascal_one_line


class TestSuite(TestCase):
    def test_resolve_name_by_index(self):
        assert get_pascal() == 5

    def test_get_pascal_one_line(self):
        assert get_pascal_one_line() == 5

