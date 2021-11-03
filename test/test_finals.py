from pascal import CalculateBestPrice


def test_fifty_percent_off():
    cbp = CalculateBestPrice()
    shopping_cart = [("Teddy bear", 20), ("Pen", 100)]
    assert cbp.fifty_percent_off(shopping_cart) == 60


def test_least_expensive_item_for_free():
    cbp = CalculateBestPrice()
    shopping_cart = [("Teddy bear", 20), ("stuff", 50), ("Pen", 100)]
    assert cbp.least_expensive_item_for_free(shopping_cart) == 150


def test_most_expensive_item_for_free():
    cbp = CalculateBestPrice()
    shopping_cart = [("Teddy bear", 20), ("stuff", 50), ("Pen", 100)]
    assert cbp.most_expensive_item_for_free(shopping_cart) == 70


def test_best_deal():
    cbp = CalculateBestPrice()
    shopping_cart = [("Teddy bear", 10), ("stuff", 50), ("Pen", 100)]
    assert cbp.apply_best_promotion(shopping_cart) == 60
