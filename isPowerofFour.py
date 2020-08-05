class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        li = [1<<i  for i in range(0,32,2)]
        if num in li:
            return True
        else:
            return False
        
