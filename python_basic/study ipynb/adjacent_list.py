class adjnode:
    def __init__(self, value):
        self.vartex = value
        self.next = None
class graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def add_edges(self, a, b):
        node = adjnode(a)
        node.next = self.graph[b]
        self.graph[b] = node

        node = adjnode(b)
        node.next = self.graph[a]
        self.graph[a] = node

    def printgraph(self):
        for i in range(self.V):
            print('vartex ' + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" ->{}".format(temp.vartex), end="")
                temp = temp.next
            print(" \n")

adj = graph(14)
adj.add_edges(0,1)
adj.add_edges(0,2)
adj.add_edges(0,3)
adj.add_edges(1,4)
adj.add_edges(1,5)
adj.add_edges(2,6)
adj.add_edges(2,7)
adj.add_edges(3,8)
adj.add_edges(4,9)
adj.add_edges(4,10)
adj.add_edges(6,11)
adj.add_edges(8,12)
adj.add_edges(10,13)

adj.printgraph()