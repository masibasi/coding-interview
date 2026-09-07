# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# 1466-reorder-routes-to-make-all-paths-lead-to-the-city-zero


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # think this graph as a non directed graph, then traverse.
        # if the edge does not point to 0 direction, check += 1

        graph = defaultdict(list)
        ndgraph = defaultdict(list)

        visited = set()

        for a, b in connections:
            graph[a].append(b)
            ndgraph[a].append(b)
            ndgraph[b].append(a)

        q = deque([0])

        ans = 0
        visited.add(0)

        while q:
            cur = q.popleft()
            for nxt in ndgraph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
                    if cur not in graph[nxt]:
                        ans += 1

        return ans
