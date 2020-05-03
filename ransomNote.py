from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mc = Counter()
        rc = Counter()
        mc.update(magazine)
        rc.update(ransomNote)
        for c,i in rc.items():
            if not (c in mc and mc[c] >= rc[c]):
                return False
        return True
