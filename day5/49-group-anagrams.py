# https://leetcode.com/problems/group-anagrams/
# 49-group-anagrams.py

# Ideas:
# 1. Brute Force
#   - Compare each string with every other string
#   - Check if they are anagrams by comparing character counts
#   - Time: O(n^2 * m) where n = number of strings, m = average string length
#   - Space: O(1) or O(m) for temporary storage
#   - ❌ Inefficient, likely TLE
#
# 2. HashMap with Counter
#   - Build a Counter (frequency map) for each string
#   - Compare Counters pairwise, or use Counter as a key
#   - Time: O(n * m) to build Counters + O(n^2) comparisons if naive
#   - Space: O(n * m) for storing counters
#   - ⚠️ Works but heavy, less elegant
#
# 3. Optimized: Sort + HashMap (defaultdict)
#   - Sort each string → same anagrams will share the same sorted key
#   - Use defaultdict(list) to group strings by this key
#   - Time: O(n * m log m)  (m log m for sorting each string)
#   - Space: O(n * m) (store all strings + keys)
#   - ✅ Clean, efficient, and common interview solution

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # key: sorted string, value: list of anagrams
        for s in strs:
            key = "".join(sorted(s))  # O(m log m): sorting string
            groups[key].append(s)  # defaultdict handles missing key automatically
        return list(groups.values())  # collect grouped anagrams as a list of lists
