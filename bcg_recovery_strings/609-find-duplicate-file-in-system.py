# https://leetcode.com/problems/find-duplicate-file-in-system/
# 609-find-duplicate-file-in-system


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        dup_files = defaultdict(list)

        for path in paths:
            path = path.split()
            dir_path, files = path[0], path[1:]

            for file in files:
                file = file.replace(")", "")
                file = file.split("(")
                name, content = file[0], file[1]
                dup_files[content].append(dir_path + "/" + name)

        # ans = []
        # for files in dup_files.values():
        #     if len(files) > 1:
        #         ans.append(files)
        # return ans
        return list(filter(lambda x: len(x) > 1, list(dup_files.values())))
