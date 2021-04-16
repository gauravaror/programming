class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and stack[-1][0] == i:
                elem = stack.pop()
                stack.append((elem[0], elem[1] + 1))
            else:
                stack.append((i, 1))
            if stack[-1][1] == k:
                stack.pop()
        output = ""
        for l,c in stack:
            output += l*c
        return output
            
        
                
                    
                    
                
                        
                    
        
