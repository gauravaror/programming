from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        self.seen = {}
        self.components = 0
        def dfs(node):
            for n in adjList[node]:
                if n not in self.seen:
                    self.seen[n] = True
                    dfs(n)
        for i in range(n):
            if i not in self.seen:
                self.components += 1
                dfs(i)
        return self.components
