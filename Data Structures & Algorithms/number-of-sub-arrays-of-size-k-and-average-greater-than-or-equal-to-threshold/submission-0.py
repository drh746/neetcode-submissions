class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        s = 0
        for r in range(len(arr)):
            s += arr[r]
            if r - l + 1 > k:
                s -= arr[l]
                l += 1
            if threshold * k <= s and r - l + 1 == k:
                res += 1

        return res

            