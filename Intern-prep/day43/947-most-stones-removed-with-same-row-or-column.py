# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        # X끼리 같은 친구들 모아보기
        # Y까리 같은 친구들 모아보기
        # 각 stone 마다 같은 좌표 선 상에 있는 돌들 개수 합 (X,Y 각각) 구하기
        # 개수 합이 제일 적은 친구부터 제거
        # 제거시 그 x, y 줄에 있는 돌들의 합 업데이트
        # 모든 돌의 같은선상 합이 0이 될때까지 반복

        x_nums, y_nums = defaultdict(int), defaultdict(int)
        total = defaultdict(int)

        for x, y in stones:
            x_nums[x] += 1
            y_nums[y] += 1

    def removeStones(self, stones: List[List[int]]) -> int:
        
        
        rows, cols = defaultdict(list), defaultdict(list)

        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[x].append(i)

        visited = set()

        def dfs(idx):
            visited.add(idx)
            r, c = stones[idx]
            
            # 현재 돌과 같은 '행'에 있는 돌들 방문
            for neighbor in rows[r]:
                if neighbor not in visited:
                    dfs(neighbor)
            
            # 현재 돌과 같은 '열'에 있는 돌들 방문
            for neighbor in cols[c]:
                if neighbor not in visited:
                    dfs(neighbor)
        num_groups = 0
        for i in range(len(stones)):
            if i not in visited:
                num_groups += 1 # 새로운 그룹 발견!
                dfs(i)          # 이 그룹에 연결된 모든 돌을 방문 처리(visited)
                
        # 3. 정답: 전체 돌 - 그룹 개수
        return len(stones) - num_groups
        





class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        rank = [0] * len(stones)
        self.count = 0  # 제거 가능한 돌의 개수 (Union 성공 횟수)

        # 경로 압축 (Path Compression) - 필수!
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # 재귀로 부모를 루트로 갱신
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                # Rank 기반 최적화
                if rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                
                self.count += 1  # 두 그룹이 합쳐졌으니, 돌 하나는 제거 가능해짐
                return True
            return False

        # 행, 열별로 "대표 돌의 인덱스"를 저장할 딕셔너리
        seen_row = {} 
        seen_col = {}

        for i, (r, c) in enumerate(stones):
            # 1. 현재 돌(i)이 속한 '행'에 이미 다른 돌이 있었나?
            if r in seen_row:
                union(i, seen_row[r]) # 있었으면 그 돌이랑 합침
            else:
                seen_row[r] = i       # 없으면 내가 이 행의 대표가 됨

            # 2. 현재 돌(i)이 속한 '열'에 이미 다른 돌이 있었나?
            if c in seen_col:
                union(i, seen_col[c]) # 있었으면 그 돌이랑 합침
            else:
                seen_col[c] = i       # 없으면 내가 이 열의 대표가 됨

        return self.count

        
