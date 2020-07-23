class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ppos = 0
        spos = 0
        while len(pushed) > 0 and len(popped) > 0:
            #print(pushed, popped, stack)
            if len(stack) > 0:
                if popped[ppos] == stack[0]:
                    del popped[ppos]
                    del stack[0]
                else:
                    stack.insert(0, pushed[spos])
                    del pushed[spos]
                    
            else:
                stack.insert(0, pushed[spos])
                del pushed[spos]
                
        while len(stack) > 0 and len(popped) > 0 and popped[ppos] == stack[0]:
            #print(popped, stack)
            del popped[ppos]
            del stack[0]
        if len(pushed) == 0 and len(popped) == 0:
            return True
        else:
            return False
