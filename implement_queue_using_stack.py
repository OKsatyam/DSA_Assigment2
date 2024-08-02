
#https://leetcode.com/submissions/detail/1278696266/


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            raise Exception("Empty list")
        
        while self.size > 0:
            self.stack2.append(self.stack1.pop())
            self.size -= 1

        data = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
            self.size += 1

        return data

    def peek(self) -> int:
        if self.size == 0:
            raise Exception("Empty list")
        
        while self.size > 0:
            self.stack2.append(self.stack1.pop())
            self.size -= 1

        data = self.stack2[-1]

        while self.stack2:
            self.stack1.append(self.stack2.pop())
            self.size += 1

        return data

    def empty(self) -> bool:
        return self.size == 0
