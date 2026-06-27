class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n #initially no. of nodes = no. of components

    def findParent(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        parentN1 = self.findParent(n1)
        parentN2 = self.findParent(n2) 

        if parentN1 == parentN2:
            return

        if self.rank[parentN2] > self.rank[parentN1]:
            self.parent[parentN1] = parentN2
            self.rank[parentN1]+=self.rank[parentN2]
        else:
            self.parent[parentN2] = parentN1
            self.rank[parentN2]+=self.rank[parentN1]
        
        self.count-=1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf  = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.count