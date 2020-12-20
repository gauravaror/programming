class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        root = list(range(n))
        for qid, query in enumerate(queries):
            query.append(qid)
        queries.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        start = 0
        output = [False]*len(queries)
        def parent(x):
            if root[x] != x:
                root[x] = parent(root[x])
            return root[x]
        
        def union(x,y):
            px, py = parent(x), parent(y)
            if px == py:
                return True
            root[px] = py
            return True
        
        #print("!", queries, edgeList)
        for u, v, limit, qid in queries:
            while start < len(edgeList) and edgeList[start][2] < limit:
                #print("$", start)
                union(edgeList[start][0], edgeList[start][1])
                start += 1
            #print("%", u,v, limit, qid, root, parent(u), parent(v))
            if parent(u) == parent(v):
                output[qid] = True
        return output
                
        
