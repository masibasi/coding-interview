# https://leetcode.com/problems/decode-string/
# 394-decode-string


class Solution:
    # 모든 형식에 따라 다르게 분기처리해서 만드는 방법
    def decodeString(self, s: str) -> str:
        stack = []
        str_substring = ""
        num_substring = ""
        for i, char in enumerate(s):
            if char.isnumeric():
                num_substring += s[i]
            if char.isalpha():
                str_substring += s[i]
            if char == "[":
                stack.append((num_substring, str_substring))
                str_substring = ""
                num_substring = ""
            if char == "]":
                cur_num, cur_str = stack.pop()
                str_substring = cur_str + (int(cur_num) * str_substring)

        return str_substring
