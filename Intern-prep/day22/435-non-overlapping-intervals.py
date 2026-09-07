# https://leetcode.com/problems/non-overlapping-intervals/description/
# 435-non-overlapping-intervals


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # earliest finish time sort

        last_interval = float("-inf")
        remove_count = 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start < last_interval:
                remove_count += 1
                continue
            else:
                last_interval = end

        return remove_count
