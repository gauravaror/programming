from collections import defaultdict
import copy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        nnodes = len(graph)
        seen = {}
        paths = defaultdict(list)
        stack = [0]
        paths[0].append([0])
        ndegree = [0]*nnodes
        for i in graph:
            for j in i:
                ndegree[j] += 1
        print(ndegree)
        def find_next():
            for idx,i in enumerate(ndegree):
                if i == 0:
                    return idx
            return -1
        while not(len(seen) == nnodes):
            print(stack, seen)
            now_pop = find_next()
            if now_pop < 0:
                return paths[nnodes-1]
            ndegree[now_pop] -= 1
            if now_pop in seen:
                continue
            seen[now_pop] = True
            for vert in graph[now_pop]:
                for path in paths[now_pop]:
                    npath = copy.copy(path)
                    npath.append(vert)
                    paths[vert].append(npath)
                ndegree[vert] -= 1
                stack.append(vert)
        return paths[nnodes-1]
