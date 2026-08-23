# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # longest time : start with 1
        # shortest time : max bananas in pile. -> just # of piles
        # algo for duration: 
        ## for # of piles: 
        ## while pile > 0:
        ##. pile - k
        l = 1
        r = max(piles)
        ans = float('inf')

        while l <= r:
            k = (l + r) //2
            t = 0
            for pile in piles:
                remaining = 0
                if pile % k != 0:
                    remaining = 1
                t += pile // k + remaining
            if t <= h:
                ans = min(k, ans)
                r = k - 1
            else:
                l = k + 1
        return ans