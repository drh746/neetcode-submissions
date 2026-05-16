class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_table:
                return [hash_table[diff], i]
            if n not in hash_table:
                hash_table[n] = i
        return []