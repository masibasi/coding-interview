# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        max_bloom_day = max(bloomDay)

        low = 0
        high = max_bloom_day

        ans = -1
        while low <= high:
            mid = (low + high) // 2
            print(mid)

            reamining_flowers = m
            prev_flower_count = 0
            for day in bloomDay:
                if day <= mid:
                    if prev_flower_count == k - 1:
                        prev_flower_count = 0
                        reamining_flowers -= 1
                    else:
                        prev_flower_count += 1
                else:
                    prev_flower_count = 0

            if reamining_flowers <= 0:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
