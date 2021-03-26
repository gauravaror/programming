class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        B = [Counter(b) for b in B]
        c = B[0]
        for b in B[1:]:
            for k, v in b.items():
                c[k] = max(c[k], v)
        output = []
        for a in A:
            ac = Counter(a)
            uni = True
            for k, v in c.items():
                if k not in ac  or (k in a and ac[k] < v):
                    uni = False
                    break
            if uni:
                output.append(a)
        return output
