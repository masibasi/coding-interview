        
# https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # 그래프로 생각해볼 수 있을까?

        ans = []
        def dfs(start, path):
            if len(path[:-1].split('.')) > 4:
                return
            
            if len(path) > len(s) + 3 or start >= len(s):
                if len(path[:-1].split('.')) == 4:
                    ans.append(path[:-1])
                return

            for i in range(1,4):
                if s[start] == '0':
                    dfs(start + 1, path[:] + "0.")
                    break
                elif start + i <= len(s) and 0 < int(s[start:start + i]) <= 255:
                    dfs(start + i, path[:] + s[start:start + i] + '.')

        dfs(0, "")

        return ans