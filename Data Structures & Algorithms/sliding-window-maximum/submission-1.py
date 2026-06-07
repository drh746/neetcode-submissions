class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max heap 
        # window size: r - k + 1
        import heapq
        heap = []
        res = []
        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            if r >= k - 1:
                while heap[0][1] < r - k + 1 :
                    heapq.heappop(heap)
                res.append(-heap[0][0])
                
        return res

            