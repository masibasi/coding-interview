# https://leetcode.com/problems/car-fleet/
# 853-car-fleet


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        eta = [(target - p) / s for p, s in zip(position, speed)]

        position = [(p, e) for p, e in zip(position, eta)]

        position.sort(reverse=True)

        max_eta = 0
        ans = 0
        for p, eta in position:
            if max_eta < eta:
                ans += 1
                max_eta = eta

        return ans
