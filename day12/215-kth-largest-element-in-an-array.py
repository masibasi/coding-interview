# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215-kth-largest-element-in-an-array


# Idea :
# 0. Brute force
## sort and find (nlogn)
# 1. Heap
## Kth 가 붙으면 heap을 써야하는거같다.
## I will want to use a max heap. or utilize a min heap of size k
## if max heap, put all in a max heap (), and heappop k times.
## if min heap, put all in a min heap until k elems. if root < next num, replace root with num
##  then pop k times  O(n log k)

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # Minheap
        # for i, num in enumerate(nums):
        #     if i < k:
        #         heapq.heappush(heap, num)
        #     else:
        #         if heap[0] < num:
        #             heapq.heapreplace(heap, num)

        # ans = heapq.heappop(heap)

        # Maxheap
        for num in nums:
            heapq.heappush(heap, -num)
        ans = 0
        i = 0
        while i < k:
            ans = heapq.heappop(heap)
            i += 1
        return ans * -1
