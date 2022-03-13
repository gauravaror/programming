from collections import defaultdict
from typing import List
from heapq import heappop, heappush

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj = defaultdict(list)
        radj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v,w])
            radj[v].append([u,w])
        def dijkstara(edges, source):
            distances = defaultdict(lambda: inf)
            pq = [[0, source]]
            while len(pq) > 0:
                weight, node = heappop(pq)
                if node in distances:
                    continue
                distances[node] = weight
                for n_,wei in edges[node]:
                    heappush(pq, [weight + wei, n_])
                    
            return distances
        a = dijkstara(adj, src1)
        b = dijkstara(adj, src2)
        c = dijkstara(radj, dest)
        ans = inf
        for i in range(n):
            ans = min(ans, a[i] + b[i] + c[i])
        return ans if ans != inf else -1
            
             
