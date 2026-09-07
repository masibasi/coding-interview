# https://leetcode.com/problems/merge-intervals/description/
# 56-merge-intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x : x[0])

        # start, end = intervals[0][0], intervals[0][1]
        # ans = []
        # for i in range(1, len(intervals)):
        #     a, b = intervals[i][0],  intervals[i][1]
        #     if end >= a:
        #         if end < b:
        #             end = b
        #     else:
        #         ans.append([start, end])
        #         start = a
        #         end = b

        # ans.append([start, end])
        # return ans

        res = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
