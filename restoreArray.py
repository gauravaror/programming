
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = len(adjacentPairs) + 1
        ndegree = Counter()
        graph = defaultdict(list)
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            ndegree[u] += 1
            ndegree[v] += 1
        seen = set()
        onedegree = ndegree.most_common()[-1][0]
        output = []
        stack = [onedegree]
        print(stack)
        while stack:
            elem = stack.pop()
            output.append(elem)
            seen.add(elem)
            for i in graph[elem]:
                if i not in seen:
                    stack.append(i)
                
        return output
            
            
        
            
        
