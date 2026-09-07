# https://leetcode.com/problems/koko-eating-bananas/
# 875-koko-eating-bananas


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        # Edge cases:
        if n == h:
            return max(piles)

        ans_max = max(piles)

        l = 1
        r = ans_max

        min_k = float("inf")
        max_time = 0
        while l <= r:
            mid = int((l + r) / 2)
            print(mid)
            count = 0
            for pile in piles:
                quotient, remainder = divmod(pile, mid)
                count += quotient
                count += 0 if remainder == 0 else 1
            if count <= h:  # this means you ate too fast. (could be ans)
                r = mid - 1
                if count >= max_time:
                    max_time = count
                    min_k = min(min_k, mid)
            elif count > h:  # this means koko ate too slow
                l = mid + 1

        return min_k


## optimal
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(speed: int) -> bool:
            time = 0
            for pile in piles:
                time += (pile + speed - 1) // speed  # == ceil(pile / speed)
            return time <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid  # 가능한 경우 → 더 작은 k를 찾아보기
            else:
                left = mid + 1  # 너무 느림 → 더 큰 k가 필요

        return left
