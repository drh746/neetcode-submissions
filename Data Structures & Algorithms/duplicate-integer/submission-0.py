class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        toto = set(nums)
        return len(toto) != len(nums)
