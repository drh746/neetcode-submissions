class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            cur = i + 1
            while cur < len(prices):
                if prices[cur] > prices[i]:
                    res = max(res, prices[cur] - prices[i])
                cur += 1
        return res
