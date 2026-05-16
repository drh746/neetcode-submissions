class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 1. iterate the list and put the count as key and num as value
        # # 2. sort the key and return the value
        # dict = {}
        # for num in nums:
        #     dict[num] = 1 + dict.get(num, 0)
        # arr = []
        # for num, freq in dict.items():
        #     arr.append([freq, num])
        # arr.sort()
        # res = []
        # while k > 0:
        #     res.append(arr.pop()[1])
        #     k -= 1
        # return res


        import heapq
        heap = []
        dict = {}
        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        for num, freq in dict.items():
            heapq.heappush(heap, [freq, num])
        while(len(heap) > k):
            heapq.heappop(heap)
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])

        return res
