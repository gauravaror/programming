from collections import defaultdict
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # Recursive function to return gcd of a and b 
        def gcd(a,b): 
            # Everything divides 0  
            if (b == 0): 
                 return a 
            return gcd(b, a%b) 
        edge_list = defaultdict(set)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                #print("dfs", i,j, A[i], A[j])
                gd = gcd(A[i], A[j])
                if gd > 1:
                    edge_list[gd].add(A[j])
                    edge_list[gd].add(A[i])
        
        keys = list(edge_list.keys())
        new_edge_list = defaultdict(list)
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                if len(edge_list[keys[i]] & edge_list[keys[j]]) > 0:
                    new_edge_list[keys[i]].append(keys[j])
                    new_edge_list[keys[j]].append(keys[i])
                    
        edge_list_p = edge_list
        edge_list = new_edge_list
        seen = {}
        component = []
        self.maxitem = 0
        print("length", len(edge_list))
        #return len(edge_list)
        def dfs(node):
            for adjVert in edge_list[node]:
                if adjVert not in seen:
                    component[-1] += len(edge_list_p[adjVert])
                    seen[adjVert] = True
                    dfs(adjVert)
                    if component[-1] > self.maxitem:
                        self.maxitem = component[-1]
        for i in A:                
            if i not in seen:
                seen[i] = True
                component.append(1)
                dfs(i)
        return self.maxitem
