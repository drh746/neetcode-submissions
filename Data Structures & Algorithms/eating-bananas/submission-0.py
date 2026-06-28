class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles) + 1
        res = max(piles)
        
        while l < r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            if hours <= h:
                res = min(res, k)
                r = k
            else:
                l = k + 1
        return res


