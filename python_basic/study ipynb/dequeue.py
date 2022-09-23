from asyncio import queues


class node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class dequeue:
    def __init__(self):
        self.head = None
        self.h = 0
        self.tail = None
        self.t = 0

    def right_push(self, data):
        if self.head == None:
            self.head = node(data)
            self.tail =  self.head
        else:
            self.tail.next = node(data, prev = self.tail)
            self.tail = self.tail.next
        self.t += 1

    def left_push(self, data):
        if self.head == None:
            self.head = node(data)
            self.tail =  self.head
        else:
            self.head.prev = node(data, next = self.head)
            self.head = self.head.prev
        self.h -= 1

    def left_pop(self):
        if self.h == self.t:
            print("Queue is empty!!!")
        else:
            print(self.head.data)
            self.head = self.head.next
            self.h += 1

    def right_pop(self):
        if self.h == self.t:
            print("Queue is empty!!!")
        else:
            print(self.tail.data)
            self.tail = self.tail.prev
            self.tail.next = None
            self.t -= 1       
    
    def printall(self):
        current1 = self.head
        while(current1):
            print(current1.data)
            current1 = current1.next

ll = dequeue()
ll.left_push(10)
ll.right_push(3)
ll.left_push(13)
ll.right_push(12)
ll.left_push(50)
ll.left_push(15)
#ll.search(8)
ll.left_pop()
ll.right_pop()
ll.right_pop()
print('------------------------------')
# ll.enqueue(3)
# ll.enqueue(4)
# ll.enqueue(5)
# ll.enqueue(6)
ll.printall()

