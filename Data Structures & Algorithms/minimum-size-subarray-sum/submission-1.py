class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # add the sum
        # window：sum >= target
        l = 0
        sum = 0
        import sys
        res = sys.maxsize
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                res = min(res, r - l + 1)
                sum -= nums[l]
                l += 1
        return res if res != sys.maxsize else 0
