class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        deletion = 0
        for l in zip(*A):
            st = l[0]
            for k in l[1:]:
                if ord(k) - ord(st) < 0:
                    deletion += 1
                    break
                st = k
        return deletion
