from collections import defaultdict

class Graph:
    def __init__(self, num):
        self.v = num
        self.graph = defaultdict(list)
        self.visited = [False] * self.v

    def add_edges(self, u, v):
        self.graph[u].append(v)

    def topSort_(self, v, stack):
        self.visited[v] = True
        for i in self.graph[v]:
            if self.visited[i] == False:
                self.topSort_(i, stack)
        stack.insert(0,v)
    
    def topSort(self):
        stack = []
        for i in range(self.v):
            if self.visited[i] == False:
                self.topSort_(i, stack)
        print(stack)

    def printgraph(self):
        for i in range(self.v):
            print('vartex ' + str(i) + ":", end="")
            print(self.graph[i])

adj= Graph(6)
adj.add_edges(0,2)
adj.add_edges(1,2)
adj.add_edges(2,3)
adj.add_edges(2,4)
adj.add_edges(2,5)
adj.add_edges(5,3)
adj.add_edges(4,3)
adj.add_edges(4,5)

adj.topSort()

adj.printgraph()
