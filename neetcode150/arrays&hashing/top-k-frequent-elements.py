# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use counter
        count = Counter(nums)
        heap = []
        for num in count:
            heapq.heappush(heap, (-count[num], num)) #minheap

        ans = []
        for i in range(k):
            # heap - [0] : -freq, [1] : num
            ans.append(heapq.heappop(heap)[1])

        return ans

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        buckets = defaultdict(list)
        count = Counter(nums)

        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                ans.append(num)
                k -= 1
            if k == 0:
                return ans
