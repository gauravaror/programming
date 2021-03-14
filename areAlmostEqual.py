class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        n = len(s1)
        mismatch = []
        for i in range(n):
            if s1[i] != s2[i]:
                mismatch.append(i)
        if len(mismatch) > 2 or len(mismatch) == 1:
            return False
        if len(mismatch) == 0:
            return True
        if len(mismatch) == 2:
            m1, m2 = mismatch
            if s1[m1] == s2[m2] and s1[m2] == s2[m1]:
                return True
        return False
        
