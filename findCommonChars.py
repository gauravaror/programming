class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        prev = Counter()
        curr = Counter()
        prev.update(A[0])
        for this in A[1:]:
            for ind in this:
                if ind in prev and prev[ind] > 0:
                    prev[ind] -= 1
                    curr[ind] += 1
            prev = curr
            curr = Counter()
        output = []
        for k, v in prev.items():
            output.extend([k]*v)
        return output
        
        
