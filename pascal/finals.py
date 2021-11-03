class CalculateBestPrice:
    def fifty_percent_off(self, products):
        return sum(cost for _, cost in products) * 0.5

    def least_expensive_item_for_free(self, products):
        prices = [cost for product, cost in products]
        prices.sort()
        return sum(prices[1:])

    def most_expensive_item_for_free(self, products):
        prices = [cost for product, cost in products]
        prices.sort()
        return sum(prices[:-1])

    def apply_best_promotion(self, products):
        available_promotions = [
            self.fifty_percent_off,
            self.least_expensive_item_for_free,
            self.most_expensive_item_for_free,
        ]
        return min(promotion(products) for promotion in available_promotions)
