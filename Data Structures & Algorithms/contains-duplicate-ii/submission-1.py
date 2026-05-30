class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        exist = set()
        for r in range(len(nums)):
            if r - l > k:
                exist.remove(nums[l])
                l += 1
            if nums[r] in exist:
                return True
            exist.add(nums[r])
        return False
            


