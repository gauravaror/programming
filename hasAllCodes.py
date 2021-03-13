class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        g = set()
        for i in range(len(s)-k+1):
            g.add(s[i:i+k])
            
        for i in range(2**k):
            ch = (bin(i)[2:].zfill(k))
            if ch not in g:
                return False
        return True
        
