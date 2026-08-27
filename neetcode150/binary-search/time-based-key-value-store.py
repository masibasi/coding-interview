# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.keys[key]) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            t,v  = self.keys[key][mid]
            if t <= timestamp:
                ans = v
                l = mid + 1
            else:
                r = mid - 1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)