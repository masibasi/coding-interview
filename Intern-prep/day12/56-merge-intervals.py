# https://leetcode.com/problems/merge-intervals/
# 56-merge-intervals

# Ideas

# 1. Brute Force
## examine every overlap starting from 1st.
## if overlap, merge and re-search
## -> n^3


# 2.
## 시작 값으로 정렬한다
## result 리스트 끝값의 end > i의 start이면 merge 후 리스트 저장
## 아니면 그냥 리스트 저장
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans_list = []

        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            s, e = interval[0], interval[1]
            if len(ans_list) == 0:
                ans_list.append(interval)
            else:
                compare = ans_list[-1]
                cs, ce = compare[0], compare[1]
                if ce >= s:
                    ans_list[-1] = [cs, max(e, ce)]
                else:
                    ans_list.append(interval)
        return ans_list
