# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        graph = defaultdict(list)
        counter_strs = []

        for og_str in strs:
            counter_strs.append(Counter(og_str))

        for i in range(n):
            graph[i] = []
            for j in range(i + 1, n):
                if counter_strs[i] == counter_strs[j]:
                    graph[i].append(j)
                    graph[j].append(i)

        ans = []
        seen = set()

        for s in graph:
            if s in seen:
                continue
            temp = []
            temp.append(strs[s])
            seen.add(s)
            for t in graph[s]:
                temp.append(strs[t])
                seen.add(t)
            ans.append(temp)

        return ans


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())