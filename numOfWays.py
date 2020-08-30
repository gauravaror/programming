import math 
class Solution:
    def solve(self, nums):
        if len(nums) <= 1:
            return 1
        head = nums[0]
        bigger = []
        smaller = []
        for i in nums[1:]:
            if i > head:
                bigger.append(i)
            else:
                smaller.append(i)
        total = math.comb(len(bigger) + len(smaller), len(smaller))
        return total*self.solve(smaller)*self.solve(bigger)
        
        
    def numOfWays(self, nums: List[int]) -> int:
        return (self.solve(nums) -1)%1000000007
