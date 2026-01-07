# https://leetcode.com/problems/contains-duplicate/description/
# 217-contains-duplicate
import heapq
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for freq in count.values():
            if freq > 1:
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False        
        heapq.heapify(nums)


        prev = None

        while nums:
            cur = heapq.heappop(nums)
            print(cur)
            if prev == cur:
                return True
            prev = cur

        return False
