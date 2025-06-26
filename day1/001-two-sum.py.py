# my thoughts :
# the nums arrays are not sorted.
# I will start with a naive solution
# I should use two nested arrays, pick the first index, check with all other indices
## **Brute force solution**
# for i in range(len(nums)):
# for j in range(i + 1, len(nums)): ## wow I used so much time writing this nested loop...
# if nums[i] + nums[j] == target:
# return [i,j]
## Correct! This was the brute force version.
## this is O(n2) since the loops are nested, containing n (size of the nums list) access.
## Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
## If the first integer is already bigger or equal with the target, I may move on to the next i. (will it reduce my big O ? I think no)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## I think I may use a temp Set of numbers that I want to see in the rest of the nums list. so if I found 2, I will be storing 7 for sum of 9. but how will i output the correct index? maybe I shall use List -> Oh I shall use Dict. But how will it reduce my bigO?
        ## Answer checked in ChatGPT : use Hash map
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


# 🧠 기억해야 할 건 딱 2가지!
# 	1.	dict, set, map 등은 해시 기반 → 평균 탐색 시간 O(1)
# 	2.	if x in dict: → 내부적으로 해시값 계산 후 위치 확인
