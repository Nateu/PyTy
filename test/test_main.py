from unittest import TestCase
from pascal import get_pascal


class TestSuite(TestCase):
    def test_resolve_name_by_index(self):
        assert get_pascal() == 5

