class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        for i in edges:
            indegree[i[1]] += 1
        return [ idx for idx,i in enumerate(indegree) if i == 0 ]
