
#https://leetcode.com/submissions/detail/1279396226/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        trav = self.head
        for _ in range(index):
            trav = trav.next
        
        return trav.data

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            print(f"Invalid index {index}")
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            trav = self.head
            for _ in range(index - 1):
                trav = trav.next
            newNode = Node(val)
            newNode.next = trav.next
            trav.next = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
            

        if index == 0:
            temp = self.head
            self.head = self.head.next
            if self.size == 1: 
                self.tail = None
            del temp
        else:
            trav1 = self.head
            for _ in range(index - 1):
                trav1 = trav1.next
            trav2 = trav1.next
            trav1.next = trav2.next
            if index == self.size - 1: 
                self.tail = trav1
            del trav2

        self.size -= 1

# Example usage:
# obj = MyLinkedList()
# print(obj.get(index))
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)