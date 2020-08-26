"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import defaultdict
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        indegree = {}
        stack = []
        value = {}
        outedge = {}
        for i in range(len(employees)):
            eid = employees[i].id
            
            indegree[eid] = (len(employees[i].subordinates), employees[i])
            
            for sub in employees[i].subordinates:
                outedge[sub] = eid
                
            if indegree[eid][0] == 0:
                stack.append(eid)
        
        while len(stack) > 0:
            elem = stack.pop()
            myimp = indegree[elem][1].importance
            
            if elem in outedge:
                indegree[outedge[elem]] = (indegree[outedge[elem]] [0]-1, indegree[outedge[elem]][1])
                if indegree[outedge[elem]][0] == 0:
                    stack.append(outedge[elem])
                    
            for el in indegree[elem][1].subordinates:
                myimp += value[el]
            value[elem] = myimp
        return value[id]
