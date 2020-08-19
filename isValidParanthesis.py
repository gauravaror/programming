class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        idx = 0
        hh = {')':'(', ']': '[', '}': '{'}
        while idx < len(s):
            #print(idx, s, stack)
            if s[idx] in ['(', '[', '{']:
                stack.insert(0, s[idx])
            else:
                #print(stack)
                if len(stack) == 0:
                    return False
                topelem = stack.pop(0)
                #print(topelem, s[idx])
                if hh[s[idx]] != topelem:
                    return False
            idx += 1
        #print(stack)
        return len(stack) == 0
