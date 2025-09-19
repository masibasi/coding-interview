# https://leetcode.com/problems/course-schedule/
# 207-course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        taken = 0

        while q:
            cur = q.popleft()
            taken += 1
            for course in graph[cur]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return taken == numCourses