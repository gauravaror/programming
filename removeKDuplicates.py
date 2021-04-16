class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def removeKDuplicates(d):
            start = 0
            end = 0
            removed = False
            output = ""
            while start < len(d):
                if end < len(d) and d[start] == d[end]:
                    end += 1
                else:
                    output += d[start:end]
                    start = end
                if (end-start) == k:
                    removed = True
                    start = end
            return output, removed
        
        removed = True
        while removed:
            s, removed = removeKDuplicates(s)
        return s
