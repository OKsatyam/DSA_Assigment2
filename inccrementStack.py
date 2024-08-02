#https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.customStack = []
        self.incrementStack = []
        self.size = 0
        self.maxsize = maxSize

    def push(self, x: int) -> None:
        if self.size == self.maxsize:
            return
        self.customStack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return -1
        self.size -= 1
        return self.customStack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.customStack[i] += val

    def empty(self) -> bool:
        return self.size == 0


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k, val)
