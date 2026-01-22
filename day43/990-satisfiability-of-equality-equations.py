# https://leetcode.com/problems/satisfiability-of-equality-equations/description/


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        stack = []
        parent = [n for n in range(26)]
        rank = [0 for _ in range(26)]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(a, b):
            p_a, p_b = find(a), find(b)
            if p_a != p_b:
                if rank[p_a] < rank[p_b]:
                    parent[p_a] = p_b
                elif rank[p_a] > rank[p_b]:
                    parent[p_b] = p_a
                else:
                    parent[p_b] = p_a
                    rank[p_b] += 1

        for e in equations:
            a, b = ord(e[0]) - ord("a"), ord(e[3]) - ord("a")
            if e[1] == "=":
                union(a, b)
            elif e[1] == "!":
                stack.append((a, b))

        while stack:
            x, y = stack.pop()
            if find(x) == find(y):
                return False

        return True
