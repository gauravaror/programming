class Solution:
    def customSortString(self, order: str, str: str) -> str:
        c = Counter(str)
        output = ""
        for i in order:
            if i in c:
                output += i*c[i]
                del c[i]
        for i,j in c.items():
            output += i*j
        return output
        
