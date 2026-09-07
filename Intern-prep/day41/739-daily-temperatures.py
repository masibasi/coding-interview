# https://leetcode.com/problems/daily-temperatures/?envType=problem-list-v2&envId=plakya4j

# 739-daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        number_of_days_to_wait = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((day, temp))
                continue
            elif stack[-1][1] >= temp:
                stack.append((day, temp))
                continue

            while stack and stack[-1][1] < temp:
                prev_day, _ = stack.pop()
                number_of_days_to_wait[prev_day] = day - prev_day
            stack.append((day,temp))

        return number_of_days_to_wait