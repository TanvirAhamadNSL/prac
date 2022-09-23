class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class stack:
    def __init__(self):
        self.size = 0
        self.head = None
    
    def isempty(self):
        return self.head == none

    def push(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            self.head = node(data, next=self.head)
            self.size += 1

    def pop(self):
        if self.head == None:
            raise Exception("stack is Empty!")
        current = self.head
        self.head = current.next
        self.size += 1
        return current.data

    def printall(self):
        current1 = self.head
        while(current1):
            print(current1.data)
            current1 = current1.next
    def peek(self):
        return self.head.data

ss = stack()
ss.push(5)
ss.push(4)
ss.push(3)
ss.push(2)
ss.push(1)
print(ss.pop())
print(ss.peek())
print("-------------------")
ss.printall()
        