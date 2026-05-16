class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. iterate the list and put the count as key and num as value
        # 2. sort the key and return the value
        dict = {}
        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        arr = []
        for num, freq in dict.items():
            arr.append([freq, num])
        arr.sort()
        res = []
        print(arr)
        while(k > 0):
            res.append(arr.pop()[1])
            k -= 1
        print(res)
        return res
