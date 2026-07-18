# https://leetcode.com/problems/car-fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        remaining = [target - p for p in position]
        remaining_time = [r / s for r, s in zip(remaining, speed)]

        arriving_cars = sorted(zip(position, remaining_time), reverse=True)

        prev_t = 0
        ans = 0
        for p, t in arriving_cars:
            if t <= prev_t:
                continue
            else:
                prev_t = t
                ans += 1

        return ans