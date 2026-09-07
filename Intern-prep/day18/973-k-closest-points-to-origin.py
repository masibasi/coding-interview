# https://leetcode.com/problems/k-closest-points-to-origin/
# 973-k-closest-points-to-origin


# Idea L k closest : heap


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heap.append((dist, [x, y]))

        heapq.heapify(heap)

        ans = []
        for i in range(k):
            dist, point = heapq.heappop(heap)
            ans.append(point)

        return ans


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
