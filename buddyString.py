class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        diffpos = []
        if len(A) != len(B) or len(A) <= 1:
            return False
        samechars = Counter()
        for i in range(len(A)):
            if A[i] != B[i]:
                diffpos.append(i)
            samechars[A[i]] += 1
        if len(diffpos) == 0 and samechars.most_common()[0][1] > 1:
            return True
        if len(diffpos) != 2:
            return False
        f = diffpos[0]
        s = diffpos[1]
        if A[f] == B[s] and A[s] == B[f]:
            return True
        return False
