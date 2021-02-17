class Solution(object):
    def isBipartite(self, graph):
        colors = {}
        def do_color(node, color):
            for ch in graph[node]:
                if ch in colors and color^1 == colors[ch]:
                    return False
                elif ch not in colors:
                    colors[ch] = color
                    if not do_color(ch, color^1):
                        return False
            return True
        stat = True
        for i in range(len(graph)):
            #print("fff", i)
            if i not in colors:
                colors[0] = 0
                stat = stat and do_color(i, 1)
                #print(colors, stat, i)
        return stat
                    
