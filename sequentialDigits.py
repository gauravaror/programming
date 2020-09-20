class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        self.output = []
        def backtrack(lastdigit, current_num):
            if current_num >= low and current_num <= high:
                self.output.append(current_num)
            if current_num > high:
                return
            if lastdigit == 9:
                return
            if lastdigit:
                backtrack(lastdigit+1, current_num*10 + (lastdigit+1))
            else:
                for i in range(1,9):
                    backtrack(i, i)
        backtrack(None, 0)
        return sorted(self.output)
                    
