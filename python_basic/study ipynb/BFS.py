from collections import defaultdict

class Graph:
    def __init__(self,):
        self.graph = defaultdict(list)

    def add_edges(self, a,b):
        self.graph[a].append(b)
    
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        q = []
        q.append(s)
        visited[s] = True
        while q:
            s = q.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True


adj = Graph()
adj.add_edges(5,2)
adj.add_edges(5,0)
adj.add_edges(4,0)
adj.add_edges(4,1)
adj.add_edges(3,1)
adj.add_edges(2,3)


print ("Following is Breadth First Traversal"
                  " (starting from vertex 0)")
adj.BFS(3)