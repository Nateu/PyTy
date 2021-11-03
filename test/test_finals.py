from unittest import TestCase
from pascal.finals import fifty_percent_off, least_expensive_item_for_free, most_expensive_item_for_free

class TestSuite(TestCase):
    def test_fifty_percent_off(self):
        shopping_cart = [
            ("Teddy bear", 20),
            ("Pen", 100)
        ]
        assert fifty_percent_off(shopping_cart) == 60

    def test_least_expensive_item_for_free(self):
        shopping_cart = [
            ("Teddy bear", 20),
            ("stuff", 50),
            ("Pen", 100)
        ]
        assert least_expensive_item_for_free(shopping_cart) == 150

    def test_most_expensive_item_for_free(self):
        shopping_cart = [
            ("Teddy bear", 20),
            ("stuff", 50),
            ("Pen", 100)
        ]
        assert most_expensive_item_for_free(shopping_cart) == 70
