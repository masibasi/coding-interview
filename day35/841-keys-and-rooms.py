# https://leetcode.com/problems/keys-and-rooms/description/
# 841-keys-and-rooms


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # what if I think this as a graph? or a tree
        graph = defaultdict(list)

        for i, keys in enumerate(rooms):
            for key in keys:
                graph[i].append(key)

        visited = set()

        q = deque([(0, graph[0])])

        while q:
            for _ in range(len(q)):
                room, nxt_rooms = q.popleft()

                visited.add(room)
                for nxt in nxt_rooms:
                    if nxt not in visited:
                        q.append((nxt, graph[nxt]))

        return len(visited) == len(rooms)
