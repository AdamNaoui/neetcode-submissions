class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        curr_buy=None

        for price in prices:
            if curr_buy is None or curr_buy >price:
                curr_buy=price
                continue
            max_profit=max(max_profit,price-curr_buy)
        return max_profit
        