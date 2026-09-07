# https://leetcode.com/problems/top-k-frequent-elements/
# 347-top-k-frequent-elements


# Idea:
# 1. Brute Force
## count all array -> n
## store in separate array for the counts -> space n
## sort the array -> nlogn
## return the list :k

# 2. Heap
## count all data / store in dict -> O(n)
## heapify -> O(n)
## pop

import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        heap = []
        for num in count:
            heap.append((-count[num], num))

        print(count, heap)
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
