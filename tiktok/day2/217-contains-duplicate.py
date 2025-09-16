# https://leetcode.com/problems/contains-duplicate/
# 217-contains-duplicate

# 1. Brute Force
## compare all elements for all other -> O(n)

# 2. Hash set
## store val in a set
## check if key is found


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
