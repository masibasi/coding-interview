# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Ideas :
# 1. Brute Force
## - Nested loop to search every char in both str
## - compare every char. if one is same, store in a list. check the char in str2 as found
# 2. Use Set
## - I would use set, or use Counter to compare the chars as key and frequency as value.
## - Compare the keys and values with for in syntax.
## - push the key into an returning list


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)

        result = []
        for num in counter_1:
            if num in counter_2:
                for i in range(min(counter_1[num], counter_2[num])):
                    result.append(num)

        return result
