# https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        print(counter)
        for item, value in counter.items():
            if value > float(len(nums) / 2):
                return item
