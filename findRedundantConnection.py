class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        max_edge = max(edges, key=lambda x: x[1])[1]
        root = list(range(max_edge+2))
        size = [-1]*(max_edge+2)
        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]
        def union(node1, node2):
            x,y = find(node1), find(node2)
            if x == y:
                return False
            if size[x] == -1 and size[y] == -1:
                size[x] = 2
                root[y] = x
            elif size[y] > size[x]:
                x,y = y,x
            root[y] = x
            size[x] += size[y]
            return True
        #edges = sorted(edges, key=lambda x: x[0])
        for i in edges:
            if not union(i[0], i[1]):
                return i
        return -1
