class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        l = 0
        res = 0
        for r in range(len(s)):
            # char in set:
            #   l + 1, remove char
            # char not in set:
            #   r + 1, add char, len + 1
            while s[r] in sub_string:
                sub_string.remove(s[l])
                l += 1
            sub_string.add(s[r])
            res = max(res, r - l + 1)
        return res