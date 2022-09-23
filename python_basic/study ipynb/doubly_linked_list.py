class node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
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

    def dele(self, data):
        current = self.head
        while(current):
            if current.data == data and current == self.head:
                self.head = current.next
                break
            elif current.data == data and current == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
                break
            elif current.data == data:
                prev4 = current.prev
                prev4.next = current.next
                next4 = current.next
                next4.prev = current.prev
                break
            current = current.next

    def printall(self):
        current1 = self.head
        while(current1):
            print(current1.data)
            current1 = current1.next

    def search(self, data):
        current3 = self.head
        i = 1
        flag = True
        while(current3):
            if current3.data == data:
                Flag = False
                print('{}th element'.format(i))
                break
            if current3.next == None:
                print('Not found')
            current3 = current3.next
            i += 1
    def revprint(self):
        current3 = self.tail
        while(current3):
            print(current3.data)
            current3 = current3.prev

ll = linkedlist()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
#ll.search(8)
ll.dele(8)
ll.revprint()

