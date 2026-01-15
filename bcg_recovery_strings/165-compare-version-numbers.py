# https://leetcode.com/problems/compare-version-numbers/
# 165-compare-version-numbers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_split, ver2_split = version1.split("."), version2.split(".")
        n, m = len(ver1_split), len(ver2_split)
        division_size = max(n, m)

        for i in range(division_size):
            if n >= i + 1 and m >= i + 1:
                if int(ver1_split[i]) > int(ver2_split[i]):
                    return 1
                elif int(ver1_split[i]) < int(ver2_split[i]):
                    return -1
            elif n >= i + 1:
                if int(ver1_split[i]) == 0:
                    continue
                else:
                    return 1
            elif m >= i + 1:
                if int(ver2_split[i]) == 0:
                    continue
                else:
                    return -1
        return 0
