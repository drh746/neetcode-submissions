class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            # pop
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if dq[0] < l:
                dq.popleft()
            if r + 1 >= k:
                res.append(nums[dq[0]])
                l += 1
        return res