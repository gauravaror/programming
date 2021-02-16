class Solution(object):
    def letterCasePermutation(self, s):
        output = set()
        def backtrack(st, index):
            if index >= len(s):
                output.add(st)
                return
            if st[index].isalpha():
                if ord(st[index]) <= 90:
                    backtrack(st[:index] + chr(ord(st[index]) + 32) + st[index+1:], index+1)
                else:
                    backtrack(st[:index] + chr(ord(st[index]) - 32) + st[index+1:], index+1)
            backtrack(st, index+1)
        backtrack(s, 0)
        return output
        
                
