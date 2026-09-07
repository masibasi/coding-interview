# https://leetcode.com/problems/merge-sorted-array/
# Ideas :
# 1. start from back
# - O(n + m)
#


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1  # nums1의 마지막 인덱스

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # nums2에 남은 값이 있다면 복사
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
