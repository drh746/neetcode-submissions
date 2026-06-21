class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        res = [0] * len(height)
        while l <= r:
            if maxL <= maxR:
                res[l] = maxL - height[l] if maxL - height[l] > 0 else 0
                maxL = max(maxL, height[l])
                l += 1
            else:
                res[r] = maxR - height[r] if maxR - height[r] > 0 else 0
                maxR = max(maxR, height[r])
                r -= 1
        return sum(res)
