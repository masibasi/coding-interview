# https://leetcode.com/problems/min-stack/
# 155-min-stack

# Min is easy, but min shall change when min val is pop.
# So I should put them all in order?
# If I sort the array every time, it would take time.
# will I have to use some kind of data structure like binary tree?
# or will set() or something already has min checking stuff??


# 1. use main, min stack
class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.min_stack.pop()
        self.main_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
