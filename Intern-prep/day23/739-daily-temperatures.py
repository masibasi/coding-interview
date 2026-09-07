# https://leetcode.com/problems/daily-temperatures/?envType=problem-list-v2&envId=plakya4j

# 739-daily-temperatures


class Solution:
    # Brute Force
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        ans = [0 for _ in range(n)]
        for i in range(n):
            day_count = 0
            for j in range(i, n):
                if i != j:
                    day_count += 1
                if temperatures[i] < temperatures[j]:
                    break
                if j == n - 1:
                    day_count = 0
            ans[i] = day_count

        return ans

    # Optimized
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
