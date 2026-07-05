class TimeMap:

    def __init__(self):
        self.keyStore = {} # [[timestamp, val]]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        ans = self.keyStore[key]
        l, r = 0, len(ans) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if ans[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return ans[r][1] if l > 0 else ""
        
