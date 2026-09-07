# https://leetcode.com/problems/merge-intervals/
# 56-merge-intervals

# Ideas

# 1. Brute Force
## examine every overlap starting from 1st.
## if overlap, merge and re-search
## -> n^3

# 2. 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for s, e in intervals:
            if not res or s > res[-1][1]:
                res.append([s, e])          # 새 구간 시작
            else:
                res[-1][1] = max(res[-1][1], e)  # 겹치면 끝점 확장
        return res