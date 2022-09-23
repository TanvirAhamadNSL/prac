class node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            current = self.head
            while(current != None):
                if current.data > data:
                    parent = current
                    current = current.left
                else:
                    parent = current
                    current = current.right
            if parent.data>data:
                parent.left = node(data)
            else:
                parent.right = node(data)

    def printall(self):
        print(self.data)
        self.printall(self.left)
        self.printall(self.right)



ll = BST()
ll.insert(5)
ll.insert(3)
ll.insert(4)
ll.insert(6)
ll.insert(7)
ll.printall()