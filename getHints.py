from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        AD = defaultdict(lambda: 0)
        BL = []
        for i,j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                AD[i] += 1
                BL.append(j)
        for b in BL:
            if AD[b] > 0:
                AD[b] -= 1
                B += 1
        return str(A) + 'A' + str(B) + 'B'
