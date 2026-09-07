# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# https://leetcode.com/problems/first-bad-version/
# Idea : use binary search
# 1.
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n

        while start <= end:
            mid = (end + start) // 2
            if isBadVersion(mid) == True:
                if mid == 1:
                    return 1
                if isBadVersion(mid - 1) == False:
                    return mid
                end = mid - 1
            else:
                start = mid + 1
