class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_score = 0
        for s_idx in range(len(A)):
            for n_elem in range(s_idx+1, min(len(A), s_idx + 2000)):
                score = A[s_idx] + A[n_elem] + s_idx - n_elem
                if score > max_score:
                    max_score = score
        return max_score
