# https://leetcode.com/problems/network-delay-time/
# 743-network-delay-time


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # I need to create graphs
        graph = defaultdict(list)

        for s, e, t in times:
            graph[s].append((e, t))

        q = deque([(k, 0)])
        visited_time = [-1] * (n + 1)
        visited_time[0] = 0

        while q:
            for _ in range(len(q)):
                node, time = q.popleft()
                if visited_time[node] == -1:  # first time visit
                    visited_time[node] = time
                    for to_node, to_time in graph[node]:
                        q.append((to_node, time + to_time))
                elif visited_time[node] != -1:  # other visit
                    if visited_time[node] > time:  # can visit earlier
                        visited_time[node] = time
                        for to_node, to_time in graph[node]:
                            q.append((to_node, time + to_time))

        min_time = 0
        for time in visited_time:
            if time == -1:
                return -1
            min_time = max(min_time, time)

        return min_time

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, e, t in times:
            graph[s].append((e, t))

        visit_time = [float("inf")] * (n + 1)
        heap = [(0, k)]

        while heap:
            cur_time, cur_node = heapq.heappop(heap)
            if cur_time > visit_time[cur_node]:
                continue
            if cur_time < visit_time[cur_node]:
                visit_time[cur_node] = cur_time
                for node, time in graph[cur_node]:
                    heapq.heappush(heap, (cur_time + time, node))

        min_time = max(visit_time[1:])
        return -1 if min_time == float("inf") else min_time
