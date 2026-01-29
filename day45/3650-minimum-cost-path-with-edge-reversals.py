# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/?envType=daily-question&envId=2026-01-27

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u, v, cost in edges:
            # (to_node, cost, reversed)
            graph[u].append((v, cost, False))
            graph[v].append((u, cost * 2, True))

        q = deque([])
        for node, cost, rev in graph[0]:
            q.append((node, cost, rev, 0, False, [0]))# (to_node, cost, reversed, cur_sum, used_rev, visited)
            
        # print(graph)
        # print(q)

        ans = float('inf')

        while q:
            node, cost, rev, cur_sum, used_rev, visited = q.popleft()

            cur_sum += cost
            used_rev = rev or used_rev
            visited.append(node)

            if node == n-1:
                ans = min(ans, cur_sum)
            
            for to_node, to_cost, to_rev in graph[node]:
                # if to_rev and used_rev:
                #     continue
                if to_node in visited:
                    continue
                if to_node == n-1:
                    ans = min(ans, cur_sum + to_cost)
                    continue
                q.append((to_node, to_cost, to_rev, cur_sum, used_rev, visited))
                print(node, (to_node, to_cost, to_rev, cur_sum, used_rev, visited))


        return ans if ans != float('inf') else -1



class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost * 2))

        pq = [(0,0)]

        min_cost = {i : float('inf') for i in range(n)}
        min_cost[0] = 0

        while pq:
            cur_cost, node= heapq.heappop(pq)
            
            if node == n - 1:
                return cur_cost

            for to_node, cost in graph[node]:
                if cur_cost + cost < min_cost[to_node]:
                    min_cost[to_node] = cur_cost + cost
                    heapq.heappush(pq, (cur_cost + cost, to_node))

        return -1