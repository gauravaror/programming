# https://leetcode.com/problems/integer-break/
import math
class Solution:
    def __init__(self):
        self.solution = {}
        self.solution[2] = 1
        

    def integerBreak(self, n: int) -> int:
        if n in self.solution:
            return self.solution[n]
        
        max_sol = 0
        for i in range(2, math.ceil(n/2) + 1):
            left = (n - i)
            curr_solution = 1
            if left in self.solution:
                break_left = self.solution[left]
            else:
                break_left = self.integerBreak(left)
            if i in self.solution:
                break_right  = self.solution[i]
            else:
                break_right = self.integerBreak(i)
            max_sol = max(left*i, left*break_right, i*break_left, break_left*break_right, max_sol)
        self.solution[n] = max_sol
        return max_sol
            
sol = Solution()
assert sol.integerBreak(10) = 36
assert sol.integerBreak(2) = 1
assert sol.integerBreak(3) = 2
assert sol.integerBreak(4) = 4
assert sol.integerBreak(5) = 6

