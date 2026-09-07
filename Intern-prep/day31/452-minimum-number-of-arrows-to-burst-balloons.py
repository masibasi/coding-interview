# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# 452-minimum-number-of-arrows-to-burst-balloons

# idea: I think the key is to sort the points in order.
# as of start and end
# the key is to check if every point is able to be popped (keep the endpoint of each starting point)
# 소팅 하고 이거 stack에다가 넣어도 될듯? 겹치는 부분


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))

        ans = 0
        temp_int = []
        print(points)
        for s, e in points:
            if len(temp_int) == 0:
                temp_int.append((s, e))
            else:
                cur_s, cur_e = temp_int.pop()
                if cur_e < s:  # 겹치지 않을 때 pop
                    ans += 1
                    temp_int.append((s, e))
                elif s < cur_s:  # 겹치는걸 포함할 때
                    temp_int.append((cur_s, cur_e))
                    continue
                elif cur_s <= s <= cur_e:  # 겹치는게 줄어들 때
                    temp_int.append((s, cur_e))  # 겹치는 부분 줄이기
        if len(temp_int) > 0:
            ans += 1

        return ans

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points.sort(key=lambda x: x[1])  # 끝점 정렬

        arrows = 1
        arrow_pos = points[0][1]
        for s, e in points:
            if arrow_pos < s:
                arrow_pos = e
                arrows += 1

        return arrows
