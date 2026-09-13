class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sold = float("-inf")
        held = float("-inf")
        reset = 0

        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(reset, sold)