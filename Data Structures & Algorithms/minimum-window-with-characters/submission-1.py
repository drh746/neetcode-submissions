class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # shrink window: have == need
        resIdx = (-1, -1)
        resLen = float('infinity')
        countT, window = {}, {}
        l = 0
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resIdx = (l, r)
                    resLen = r - l + 1
                window[s[l]] = window.get(s[l], 0) - 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return s[resIdx[0] : resIdx[1] + 1] if resLen != float('infinity') else ""



                

                



        
