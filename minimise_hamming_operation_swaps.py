class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        dsu = DSU(len(source))
        for i in allowedSwaps:
            dsu.union(i[0], i[1])
        categories = defaultdict(list)
        for i in range(len(source)):
            categories[dsu.find(i)].append(i)
        #print(categories)
        ans = 0
        for key in categories.keys():
            sourceelem = Counter()
            targetelem = Counter()
            for index in categories[key]:
                sourceelem[source[index]] += 1
                targetelem[target[index]] += 1
            for elem, count in sourceelem.items():
                if targetelem[elem] <= count:
                    ans += (count - targetelem[elem])
        return ans
        
