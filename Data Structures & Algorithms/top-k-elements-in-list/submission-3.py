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


        # import heapq
        # heap = []
        # dict = {}
        # for num in nums:
        #     dict[num] = 1 + dict.get(num, 0)
        # for num, freq in dict.items():
        #     heapq.heappush(heap, [freq, num])
        #     if(len(heap) > k):
        #         heapq.heappop(heap)
        # res = []
        # for i in range(len(heap)):
        #     res.append(heapq.heappop(heap)[1])

        # return res

        # 1. count the freq into a dict {freq, num}
        # 2. create an arr of len(num)
        # 3. iterate through the dict, put the num under arr[freq]
        # 4. loop through the arr from the back, add the result, then k - len(arr[freq])
        dict = {}
        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        
        arr = [[] for i in range(len(nums)+1)]
        for num, freq in dict.items():
            arr[freq].append(num)
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

