class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        for char in s:
            if stack:
                prev = stack.pop()
                if prev == char:
                    continue
                stack.append(prev)
            stack.append(char)

        return "".join(stack)
