# https://leetcode.com/problems/contains-duplicate/description/
# Ideas:
## 1. Intuitive solution
## put it into a set. see if len changes
## 2. Brute force
## scan in two nested for loops
## 3. Optimized
## use hash set. see if seen[i] exist.
## 4. use Set again, from GPT
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen = {}
        # for i, num in enumerate(nums):
        #     if num in seen:
        #         return True
        #     seen[num] = i
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
