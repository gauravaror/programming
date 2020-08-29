from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hh = defaultdict(dict)
        for eqn,val in zip(equations, values):
            a,b = eqn
            hh[a][b] = val
            hh[b][a] = 1/val
        output = []
        def bfs(curr, target):
            stack = [(1, curr)]
            seen = set()
            seen.add(curr)
            while len(stack) > 0:
                currval, elem = stack.pop()
                if elem not in hh:
                    return -1
                elif elem == target:
                    return currval
                for key,val in hh[elem].items():
                    if key not in seen:
                        seen.add(key)
                        stack.append((currval*val, key))
            return -1
                
            
        for q1,q2 in queries:
            if q1 not in hh or q2 not in hh:
                output.append(-1)
                continue
            output.append(bfs(q1, q2))
        return output
