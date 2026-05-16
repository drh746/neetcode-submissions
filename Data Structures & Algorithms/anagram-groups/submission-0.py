class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        res = []
        # iterate through the strs\
        #  1.store each str into an arr if it's not exist
        #  2. if it exist, group them
        for str in strs:
            arr = [0] * 26
            for c in str:
                index = ord(c) - ord('a')
                arr[index] += 1
            if tuple(arr) not in hash:
                hash[tuple(arr)] = [str]
            else:
                hash[tuple(arr)].append(str)

        for val in hash.values():
            res.append(val)
        return res
