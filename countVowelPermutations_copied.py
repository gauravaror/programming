class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a,e,i,o,u = 1,1,1,1,1
        for g in range(n-1):
            a,e,i,o,u = e+i+u, a+i, e + o, i, o+i
        return (a+e+i+o+u) %1000000007
