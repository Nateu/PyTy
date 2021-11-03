def fifty_percent_off(products):
    # total = 0
    # for product, price in products:
    #     total += price / 2
    return sum(cost for _, cost in products) * 0.5


def least_expensive_item_for_free(products):
    prices = [cost for product, cost in products]
    prices.sort()
    return sum(prices[1:])


def most_expensive_item_for_free(products):
    prices = [cost for product, cost in products]
    prices.sort()
    return sum(prices[:-1])


available_promotions = [fifty_percent_off, least_expensive_item_for_free, most_expensive_item_for_free]


def apply_best_promotion(products, available_promotions):
    return total_cost

