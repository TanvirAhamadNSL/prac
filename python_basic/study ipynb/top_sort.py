class adjnode:
    def __init__(self, node_name):
        self.vartex = node_name
        self.next = None

class graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
        self. indegree = [0] * self.V

    def add_edges(self, a, b):
        #node = adjnode(a)
        #node.next = self.graph[b]
        #self.graph[b] = node

        node = adjnode(b)
        self.indegree[b] += 1 
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
        print(self.indegree)

    def topsort_(self, v, visited, stack):
        visited[v] = True
        while temp:
            if visited[temp.vartex] == False:
                #print(temp.vartex)
                self.topsort_(temp.vartex, visited, stack)
                temp = temp.next
        print(temp.vartex)
        stack.insert(0,temp.vartex)

    def topsort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topsort_(i, visited, stack)

        #print(stack)


                

        

adj = graph(6)
adj.add_edges(0,2)
adj.add_edges(1,2)
adj.add_edges(2,3)
adj.add_edges(2,4)
adj.add_edges(2,5)
adj.add_edges(5,3)
adj.add_edges(4,3)
adj.add_edges(4,5)


adj.printgraph()

adj.topsort()