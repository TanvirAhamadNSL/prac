class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = node(data)
        if (self.head == None):
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node

    def dele(self, data):
        current2 = self.head
        while(current2):
            if current2.data == data and current == self.head:
                self.head = current2.next
                break
            elif current2.data == data:
                prev.next = current2.next
                break
            prev = current2
            current2 = current2.next

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

    def reverse(self, temp):
        if temp:
            self.reverse(temp.next)
            print(temp.data, end=' ')
        else:
            return
        


ll = linkedlist()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.search(8)
ll.dele(8)
ll.reverse(ll.head)
