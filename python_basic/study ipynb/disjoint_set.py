class disjoint_set:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            res =  self.find(self.parent[item])
            self.parent[item] = res
            return res
    
    def union(self, item1, item2):
        u = self.find(item1)
        v = self.find(item2)
        if u == v:
            print("they are alraeady friends")
        else:
            self.parent[u] = v

nodes = [1,2,3,4,5,6,7,8,9]
parent = {}
for i in nodes:
    parent[i] = i
ds = disjoint_set(nodes, parent)
ds.union(1,2)
ds.union(3,1)
ds.union(4,3)
print(ds.find(4))
