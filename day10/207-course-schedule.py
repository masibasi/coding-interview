# https://leetcode.com/problems/course-schedule/
# 207-course-schedule

# Idea
# - false가 나오는 경우의 수
# - numCourses-1보다 큰 값이 prerequisites 에 있으면 못들음
# - 예시를 보니 사이클이 존재하면 불가한거같음 (A->B->C->A도 안되는거지)
# - 그래프를 만들어서 서칭으로 해야하나? Directed Graph를 만들 수 있을거같긴한데
# - 들을 수 있는 조건
# - prerequisite가 없다
# - prerequisite가 해결되었다
# - 항목당 prerequisite가 있는지 확인해야한다


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq = {}
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)

        # for a, b in prerequisites:
        #     if b not in prereq:
        #         prereq[b] = [a]
        #     else : prereq[b].append(a)

        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def dfs(node):
            if visited[node] == 1:  # 현재 경로에 다시 등장 → cycle
                return False
            if visited[node] == 2:  # 이미 확인된 안전한 노드
                return True

            visited[node] = 1  # 방문 중
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 2  # 방문 완료
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        print(prereq)
