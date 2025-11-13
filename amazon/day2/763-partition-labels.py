# https://leetcode.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: idx for idx, char in enumerate(s)}

        end = 0
        start = 0
        ans = []
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans
