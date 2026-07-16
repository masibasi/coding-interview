# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not temps:
                temps.append((i, temp))
            else:
                while temps and temp > temps[-1][1]:
                    prev_i, _ = temps.pop()
                    output[prev_i] = i - prev_i
                temps.append((i, temp))

        return output