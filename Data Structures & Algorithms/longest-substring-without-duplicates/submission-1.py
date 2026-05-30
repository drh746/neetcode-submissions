class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        exist = set()
        for r in range(len(s)):
            while s[r] in exist:
                exist.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            exist.add(s[r])
        return res