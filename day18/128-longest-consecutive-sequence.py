# https://leetcode.com/problems/longest-consecutive-sequence/
# 128-longest-consecutive-sequence

# Idea : it says O(N) -> no sorting.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = {}

        max_len = 0
        for num in nums:
            if num in consecutive:
                continue
            if (num - 1) in consecutive and (num + 1) in consecutive:
                seq_l = consecutive[num - 1]
                seq_r = consecutive[num + 1]
                consecutive[num] = seq_l + seq_r + 1
                consecutive[num - seq_l] = seq_l + seq_r + 1
                consecutive[num + seq_r] = seq_l + seq_r + 1
                max_len = max(max_len, seq_l + seq_r + 1)
            elif (num - 1) in consecutive:
                seq = consecutive[num - 1]
                consecutive[num] = seq + 1
                consecutive[num - seq] = seq + 1
                max_len = max(max_len, seq + 1)
            elif num + 1 in consecutive:
                seq = consecutive[num + 1]
                consecutive[num] = seq + 1
                consecutive[num + seq] = seq + 1
                max_len = max(max_len, seq + 1)
            else:
                consecutive[num] = 1
                max_len = max(max_len, 1)

        return max_len


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
