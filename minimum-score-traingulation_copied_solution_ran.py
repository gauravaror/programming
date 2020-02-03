from functools import lru_cache
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        @lru_cache(None)
        def dfs(left, right):
            if right - left  + 1 < 3:
                return 0
            minimum = float('Inf')
            for i in range(left+1, right):
                minimum = min(minimum, A[left]*A[right]*A[i] + dfs(left, i) + dfs(i, right))
            return minimum
        return dfs(0, len(A)-1)
