class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        edges = {}
        def backtrack(i, dic):
            if i >= len(source):
                return
            if source[i] not in dic:
                dic[source[i]] = {}
            backtrack(i+1, dic[source[i]])
            backtrack(i+1, dic)
        backtrack(0, edges)
        print(edges)
        needed = 0
        running_seq = None
        for i in target:
            if running_seq == None or (i not in running_seq):
                needed += 1
                if i not in edges:
                    return -1
                running_seq = edges[i]
            else:
                running_seq = running_seq[i]
        return needed
