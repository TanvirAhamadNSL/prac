class node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class queue:
    def __init__(self):
        self.head = None
        self.h = 0
        self.tail = None
        self.t = 0

    def enqueue(self, data):
        if self.head == None:
            self.head = node(data)
            self.tail =  self.head
        else:
            self.tail.next = node(data, prev = self.tail)
            self.tail = self.tail.next
            # current = self.head
            # while(current.next):
            #     current = current.next
            # current.next = node(data, prev=current)
        self.t += 1

    def dequeue(self):
        if self.h == self.t:
            print("Queue is empty!!!")
        else:
            current = self.head
            temp = current.data
            self.head = current.next
            self.h += 1
            print(temp)
            
    def printall(self):
        current1 = self.head
        while(current1):
            print(current1.data)
            current1 = current1.next

ll = queue()
ll.enqueue(3)
ll.enqueue(4)
ll.enqueue(5)
ll.enqueue(6)
ll.enqueue(7)
ll.enqueue(8)
#ll.search(8)
ll.dequeue()
ll.dequeue()
ll.dequeue()
ll.dequeue()
ll.dequeue()
ll.dequeue()
ll.dequeue()
print('------------------------------')
ll.enqueue(3)
ll.enqueue(4)
ll.enqueue(5)
ll.enqueue(6)
ll.printall()

