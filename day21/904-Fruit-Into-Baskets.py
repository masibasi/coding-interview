# https://leetcode.com/problems/top-k-frequent-words/
#
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        freq = defaultdict(list)
        max_heap = []
        for word, f in counter.items():
            # freq[f].append(word)
            max_heap.append((-f, word))

        heapq.heapify(max_heap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(max_heap)[1])

        return ans
