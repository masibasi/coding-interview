# https://leetcode.com/problems/course-schedule-ii/
# 210-course-schedule-ii

# 이전 문제와 같이 풀되, dfs로 한번 들어간 순서를 리스트에 그대로 집어넣으면 될 것 같다
# 이미 방문한 곳에 대해서는 들어가다 2가 나오면 바로 리스트 추가하면 된다.

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         graph = {i:[] for i in range(numCourses)}
#         for a, b in prerequisites:
#             graph[b].append(a)

#         visited = [0] * numCourses # 0: not visited , 1: visiting, 2: visited

#         order = []
#         cycle = False

#         def dfs(u: int) -> bool:
#             nonlocal cycle
#             if visited[u] == 1:      # 현재 경로에 다시 등장 → 사이클
#                 return False
#             if visited[u] == 2:      # 이미 처리 완료
#                 return True

#             visited[u] = 1
#             for v in graph[u]:
#                 if not dfs(v):
#                     return False
#             visited[u] = 2
#             order.append(u)          # ✅ 후위 시점에 추가 (자식 먼저, 부모 나중)
#             return True

#         for c in range(numCourses):
#             if visited[c] == 0:
#                 if not dfs(c):
#                     return []        # 사이클이면 수강 순서 없음


#         # 후위로 쌓였으니 뒤집으면 위상정렬 순서
#         order.reverse()
#         return order
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) == numCourses:
            return order
        else:
            return []
