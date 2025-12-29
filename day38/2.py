# https://leetcode.com/problems/asteroid-collision/
# 73-asteroid-collision


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 0:
            return None

        stack = [asteroids[0]]

        for i, ast in enumerate(asteroids[1:]):
            while len(stack) > 0 and stack[-1] * ast < 0 and ast < 0:
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(ast):
                    stack.pop()
                else:
                    break
            else:
                stack.append(ast)

        return stack
