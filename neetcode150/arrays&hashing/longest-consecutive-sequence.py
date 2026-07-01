# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use defaultdict
        # every time a num is included, search for -1, +1
        # if exists, update both += 1
        # also update the end (count[num+-count[num]])
        # if not, = 1
        count = defaultdict(int)
        ans = 0
        for num in nums:
            if num in count :
                continue
            if num - 1 in count and num + 1 in count:
                count[num] = count[num-1] + count[num+1] + 1
                count[num-count[num-1]] = count[num]
                count[num+count[num+1]] = count[num]
            elif num - 1 in count:
                count[num] = count[num-1] + 1
                count[num-count[num-1]] = count[num]
            elif num + 1 in count:
                count[num] = count[num+1] + 1
                count[num+count[num+1]] = count[num]
            else:
                count[num] = 1
            ans = max(ans, count[num])

        return ans
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 1
        if len(nums) == 0:
            return 0
        for num in nums_set:
            temp = 0
            if num-1 not in nums_set:
                while num in nums_set:
                    num += 1
                    temp += 1
            ans = max(ans, temp)

        return ans