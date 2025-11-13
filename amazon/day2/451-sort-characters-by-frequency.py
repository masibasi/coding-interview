import heapq
from collections import Counter

# https://leetcode.com/problems/sort-characters-by-frequency/

# use Counter
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         counter = Counter(s)

#         flipped_dict_with_lists = defaultdict(list)

#         for key, value in counter.items():
#             flipped_dict_with_lists[value].append(key)

#         print(flipped_dict_with_lists)

#         ans = ""
#         for i in range(len(s), 0, -1):
#             if i in flipped_dict_with_lists:
#                 for char in flipped_dict_with_lists[i]:
#                     for j in range(i):
#                         ans += char

#         return ans


# Use Heap
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(heap)

        ans = ""

        while heap:
            freq, char = heapq.heappop(heap)
            ans += char * (-freq)

        return ans


# Use Bucket Sort
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())

        buckets = [[] for i in range(max_freq + 1)]

        for char, freq in counter.items():
            buckets[freq].append(char)

        ans = ""
        for freq in range(max_freq, 0, -1):
            for char in buckets[freq]:
                ans += char * freq

        return ans
