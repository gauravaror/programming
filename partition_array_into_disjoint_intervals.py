# https://leetcode.com/problems/partition-array-into-disjoint-intervals/submissions/
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maximum = A[0]
        maximum_ignoring_increasing = A[0]
        prev = A[0]
        current_ans = 0
        if len(A) == 0:
            return 0
        for idx,i in enumerate(A[1:]):
            if prev > i:
                maximum = maximum_ignoring_increasing
                current_ans = idx + 1
            
            if maximum_ignoring_increasing < i:
                maximum_ignoring_increasing = i
            
            if i < maximum:
                current_ans = idx + 1
        return current_ans + 1 
