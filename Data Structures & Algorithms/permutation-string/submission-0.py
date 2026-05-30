class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window: r - l + 1 > len(s1)
        count = [0] * 26
        countTarget = [0] * 26
        l = 0
        for s in s1:
            countTarget[ord(s) - ord('a')] += 1
        for r in range(len(s2)):
            count[ord(s2[r]) - ord('a')] += 1
            while r - l + 1 > len(s1):
                count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if countTarget == count:
                return True
        return False
