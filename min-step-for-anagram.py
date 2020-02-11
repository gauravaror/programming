from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        for i in s_counter:
            if i in t_counter:
                if s_counter[i] >= t_counter[i]:
                    del t_counter[i]
                else:
                    t_counter[i] -= s_counter[i]
        return sum(t_counter.values())
