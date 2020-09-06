class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        root = list(range(n+1))
        size = [-1]*(n+1)
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
                size[y] = 0
            elif size[y] > size[x]:
                x,y = y,x
                
            if size[y] == -1:
                size[y] = 1
            
            root[y] = x
            size[x] += size[y]
            size[y] = 0
            return True
  
        used = 0
        for i in edges:
            if i[0] == 3:
                if union(i[1],i[2]):
                    used += 1

        size_both = size.copy()
        root_both = root.copy()
        print("Both", size, root)
        for i in edges:
            if i[0] == 2:
                if union(i[1], i[2]):
                    used += 1
        size_alice = size.copy()
        root_alice = root.copy()
        size = size_both.copy()
        root = root_both.copy()
        for i in edges:
            if i[0] == 1:
                if union(i[1], i[2]):
                    used += 1
        parent = find(1)
        size_bob = size.copy()
        root_bob = root.copy()
        print(size_alice, size_bob, root_alice, root_bob, used, parent)
        
        if not (size_alice[parent] == n and size_bob[parent] == n):
            return -1
        else:
            return len(edges) - used
