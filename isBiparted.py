class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for idx,i in enumerate(graph):
            if idx not in colors:
                stack = [(idx,0)]
                while stack:
                    node, color = stack.pop()
                    colors[node] = color
                    for vert in graph[node]:
                        if vert not in colors:
                            stack.append([vert, color^1])
                        else:
                            if color == colors[vert]:
                                return False
        return True
