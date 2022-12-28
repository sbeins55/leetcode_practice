def maximize_profit(prices):
    """
    Maximize the profit by choosing a single day to buy one stock and
    choosing a different day in the future to sell that stock.

    :param prices: a list of stock prices on given days
    :return: the maximum amount of possible profit given prices
    """
    left = 0
    right = 1

    max_profit = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(max_profit, profit)
        else:
            left = right

        right += 1

    return max_profit
