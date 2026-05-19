class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        last = self.stack[-1]
        del self.stack[-1]
        if last == self.min_stack[-1]:
            del self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
