class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res: int = 0
        minimumPrice: int = prices[0]

        for price in prices[1:]:
            res = max(res, price - minimumPrice)
            minimumPrice = min(minimumPrice, price)

        return res
