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
            self.head.next = self.head
            self.head.prev = self.head
            self.tail =  self.head
        else:
            self.tail.next = node(data, prev = self.tail, next = self.head)
            self.tail = self.tail.next
            self.head.prev = self.tail
            # current = self.head
            # while(current.next):
            #     current = current.next
            # current.next = node(data, prev=current)

    def dele(self, data):
        current = self.head
        while(current):
            if current.data == data and current == self.head:
                self.head = current.next
                self.head.prev = self.tail
                self.tail.next = self.head
                break
            elif current.data == data and current == self.tail:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
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
        while(current1 != self.tail):
            print(current1.data)
            current1 = current1.next
        print(current1.data)

    def search(self, data):
        current3 = self.head
        i = 1
        flag = True
        while(current3):
            if current3.data == data:
                Flag = False
                print('{}th element'.format(i))
                break
            if current3.next == self.head:
                print('Not found')
                break
            current3 = current3.next
            i += 1

    def revprint(self):
        current3 = self.tail
        while(current3 != self.head):
            print(current3.data)
            current3 = current3.prev
        print(current3.data)

ll = linkedlist()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.search(9)
ll.dele(6)
ll.printall()