
#https://leetcode.com/submissions/detail/1278744431/

import random

class RandomizedCollection:

    def __init__(self):
        self.queue = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.queue:
            self.queue.append(val)
            self.size += 1
            return False
        
        self.queue.append(val)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.queue:
            self.queue.remove(val)
            self.size -= 1
            return True
        
        return False

    def getRandom(self) -> int:
        if self.size == 0:
            raise Exception("empty")
        
        return random.choice(self.queue)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
