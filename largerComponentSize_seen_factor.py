class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        self.maxelem = max(A)
        self.parent = [i for i in range(self.maxelem+1)]
        self.size = [1]*(self.maxelem + 1)
    
        for elem in A:
            for factor in range(2, int(sqrt(elem)) + 1):
                if elem % factor == 0:
                    self.union(elem, factor)
                    self.union(elem, elem//factor)
        groups = defaultdict(int)
        maxsize = 0
        #print(self.parent)
        #print(self.size)
        for elem in A:
            group_id = self.find(elem)
            groups[group_id] += self.size[group_id]
            if groups[group_id] > maxsize:
                maxsize = groups[group_id]
        return maxsize
                    
            
            
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] =  self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px,py = self.find(x), self.find(y)
        if px == py:
            return px
        if self.size[px] > self.size[py]:
            px,py = py,px
        self.parent[px] = py
        self.size[px] += self.size[py]
        return py
