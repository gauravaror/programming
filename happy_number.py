class Solution:
    
    def next_number(self, n: str) -> str:
        n_sum = 0
        for i in n:
            n_sum +=  int(i)**2
        return str(n_sum)
        
    def isHappy(self, n: int) -> bool:
        fast = str(n)
        slow = str(n)        
        while True:
            if slow == "1" or fast == "1":
                return True
            slow = self.next_number(slow)
            fast = self.next_number(self.next_number(fast))
            print(slow)
            if slow == "1" or fast == "1":
                return True
            
            if slow == fast:
                return False
            
            
