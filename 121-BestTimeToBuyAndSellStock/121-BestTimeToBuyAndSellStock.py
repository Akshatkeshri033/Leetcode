# Last updated: 7/4/2026, 7:03:13 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit,price-min_price)
        return max_profit

        