from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = Counter()
        c.update(J)
        output = 0
        for i in S:
            if i in c:
                output += 1
        return output
