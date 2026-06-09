# https://leetcode.com/problems/contains-duplicate/


class Solution:
    # 1. put in set
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # 2. in one line
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))