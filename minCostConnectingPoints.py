class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        root = list(range(len(points)+1))
        cost = [0]*(len(points)+1)
        
        edges = {}
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        def union(x, y):
            px,py = find(x), find(y)
            if px == py:
                return False
            if cost[py] > cost[px]:
                py,px = px,py
            root[py] = px
            cost[px] += cost[py]
            cost[px] += edges[(x,y)]
            return True
        
        def dist(x,y):
            return abs(x[0] - y[0]) + abs(x[1]-y[1])
        
        newedges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                newedges.append((i,j, dist(points[i], points[j])))
                edges[(i,j)] = dist(points[i], points[j])
        cost1 = 0
        newedges = sorted(newedges, key=lambda x: x[2])
        for i in newedges:
            if union(i[0], i[1]):
                cost1 += i[2]
        return cost1
            
            
        
