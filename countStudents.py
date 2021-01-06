class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        onestu = sum(students)
        onesand = sum(sandwiches)
        if onestu == onesand:
            return 0
        else:
            if onesand > onestu:
                for idx,i in enumerate(sandwiches):
                    if i == 1:
                        onestu -= 1
                        if onestu == -1:
                            return len(sandwiches) - idx
            else:
                onestu = len(sandwiches) - onestu
                for idx,i in enumerate(sandwiches):
                    if i == 0:
                        onestu -= 1
                        if onestu == -1:
                            return len(sandwiches) - idx
                
        
        
