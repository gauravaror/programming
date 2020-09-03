class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lens = len(s)
        for i in range(1, (len(s)//2) + 1):
            if len(s) % i == 0:
                first_hash = hash(s[:i])
                #print(first_hash, i, s[:i])
                all_equal = True
                for j in range(i,len(s), i):
                    #print("second", s[j:j+1])
                    if hash(s[j:j+i]) != first_hash:
                        all_equal = False
                if all_equal:
                    return True
        return False
