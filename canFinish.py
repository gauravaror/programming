from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [0]*numCourses
        hh = defaultdict(list)
        for i in prerequisites:
            courses[i[0]] += 1
            hh[i[1]].append(i[0])
        def getzeros():
            output = []
            for idx,i in enumerate(courses):
                if i == 0:
                    output.append(idx)
            return output
        courses_done = 0
        while True:
            s = getzeros()
            if len(s) == 0:
                break
            for i in s:
                for preq in hh[i]:
                    courses[preq] -= 1
                courses[i] = -1
                courses_done += 1
        print(courses_done, courses)
        if courses_done < numCourses:
            return False
        else:
            return True
