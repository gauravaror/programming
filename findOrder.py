from collections import defaultdict,Counter
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_dict = defaultdict(list)
        preq_dict = defaultdict(list)
        preq_counter = Counter()
        for p in prerequisites:
            course_dict[p[0]].append(p[1])
            preq_dict[p[1]].append(p[0])
            preq_counter[p[0]] += 1
        
        def find_min():
            mine = numCourses + 4
            mini = -1
            for i in range(numCourses):
                 if preq_counter[i] < mine:
                        mine = preq_counter[i]
                        mini = i
            return mine, mini
        done_elem = 0
        order = []
        while done_elem < numCourses:
            mine, mini = find_min()
            #print(preq_counter, mine, mini)
            if mine != 0:
                return []
            order.append(mini)
            preq_counter[mini] = numCourses + 10
            for item in preq_dict[mini]:
                preq_counter[item] -= 1
            done_elem += 1
        return order
