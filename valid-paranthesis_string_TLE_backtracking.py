from typing import List
from copy import copy

class Solution:
    
    def checkValidString1(self, s:str, ll: List) -> bool:
        #print(s, ll)
        if (len(s) == 0 and len(ll) == 0) or (len(s) == 1 and s == "*" and len(ll) == 0):
            return True
        elif ((len(s) == 0 and (len(ll) is not 0)) or (len(s) == 1 and s == "*" and (len(ll) is not 0))):
            return False
        
        if s[0] == '*':
            ll1 = copy(ll)
            #print("Running first")
            out1 = self.checkValidString1('(' + s[1:], ll1)
            ll1 = copy(ll)
            #print("Running second")
            out2 = self.checkValidString1(')'  + s[1:], ll1)
            ll1 = copy(ll)
            #print("Running third")
            out3 = self.checkValidString1(s[1:], ll1)
            return out1 or out2 or out3
        elif s[0] == ')':
            if len(ll) == 0:
                return False
            if ll[-1] == '(':
                del ll[-1]
                return self.checkValidString1(s[1:], ll)
            else:
                return False
        else:
            ll.append(s[0])
            return self.checkValidString1(s[1:], ll)
        
    def checkValidString(self, s: str) -> bool:
        return self.checkValidString1(s, [])
