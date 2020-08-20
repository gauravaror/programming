from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(lambda: 0)
        adjList = defaultdict(list)
        for i in edges:
            adj[i[1]] += 1
            adjList[i[1]].append(i[0])
            adjList[i[0]].append(i[1])
        self.seen = {}
        self.cycle = False
        def dfs(node):
            #print("Node: ",node, edges, adjList[node], self.seen)
            for n in adjList[node]:
                #print("Node ADJ: ", n , n not in self.seen, adjList[node], self.seen)
                if n not in self.seen:
                    #print(n)
                    self.seen[n] = node
                    dfs(n)
                else:
                    if n == self.seen[node]:
                        continue
                    self.cycle = True
                    return False
                if adj[n] == 0:
                    zero_in = n
            return True
        self.seen[0] = -1
        dfs(0)
        if self.cycle:
            return False
        #print(self.seen)
        return False if len(self.seen) < n else True
