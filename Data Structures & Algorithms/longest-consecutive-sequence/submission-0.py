class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            length = 0
            while num in nums_set:
                length += 1
                num += 1
            res = max(length, res)
        return res

