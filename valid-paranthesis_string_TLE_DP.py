from typing import List
from copy import copy
from collections import Counter
from functools import lru_cache

class Solution:
    @lru_cache
    def cdp(self, pos1, pos2):
        if pos1 > pos2:
            return 1
        if pos1 == pos2 and self.str[pos1] == "*":
            return 1
        if self.dp[pos1][pos2] != -1:
            return self.dp[pos1][pos2]
        if self.str[pos1] in '*(' and self.str[pos2] in  ')*':
            if self.cdp(pos1+1, pos2-1) == 1:
                self.dp[pos1][pos2] = 1
                return 1
        for cpos in range(pos1+1, pos2):
            if self.cdp(pos1, cpos) == 1 and self.cdp(cpos+1, pos2) == 1:
                self.dp[pos1][pos2] = 1
                return 1
        return 0
        
        
            
    def checkValidString(self, s: str) -> bool:
        self.dp = [[-1]*len(s) for _  in range(len(s))]
        self.str = s
        return self.cdp(0, len(s)-1)
