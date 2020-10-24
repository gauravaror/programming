class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        start = 0
        end = len(tokens)-1
        score = 0
        mscore = 0
        tokens.sort()
        while start <= end:
            if tokens[start] <= P:
                P -= tokens[start]
                start += 1
                score += 1
            else:
                if score >= 1:
                    P += tokens[end]
                    end -= 1
                    score -= 1
                else:
                    break
            mscore = max(score, mscore)
        return mscore
