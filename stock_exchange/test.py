import unittest

from stock_exchange.solution import maximize_profit


class MaximizeProfit(unittest.TestCase):

    def test_decreasing_no_profit(self):
        prices = [10, 8, 6, 4, 2]
        max_profit = maximize_profit(prices)

        self.assertEqual(0, max_profit)

    def test_flat_no_profit(self):
        prices = [10, 10, 10, 10, 10]
        max_profit = maximize_profit(prices)

        self.assertEqual(0, max_profit)

    def test_increasing_profit(self):
        prices = [2, 4, 6, 8, 10]
        max_profit = maximize_profit(prices)

        self.assertEqual(8, max_profit)

    def test_spiking_profit(self):
        prices = [10, 2, 8, 4, 6]
        max_profit = maximize_profit(prices)

        self.assertEqual(6, max_profit)

