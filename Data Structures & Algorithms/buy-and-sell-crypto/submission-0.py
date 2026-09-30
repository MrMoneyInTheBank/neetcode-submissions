class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        mn = prices[0]

        for p in prices[1:]:
            profit = p - mn
            res = max(res, profit)
            mn = min(mn, p)

        return res
        