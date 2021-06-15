class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix_sum = list(accumulate(stones))
        @lru_cache(None)
        def pick(i, j, turn, score1, score2):
            if i == j:
                return score1, score2
            nextTurn = abs(1-turn)
            
            add_1 = prefix_sum[j] - prefix_sum[i]
            f_s1 = score1 + add_1 if turn == 0 else score1
            f_s2 = score2 + add_1 if turn == 1 else score2
            first = pick(i+1, j, nextTurn, f_s1, f_s2)
            
            a = prefix_sum[i-1] if i > 0 else 0
            add_2 = prefix_sum[j-1] - a
            s_s1 = score1 + add_2 if turn == 0 else score1
            s_s2 = score2 + add_2 if turn == 1 else score2
            second = pick(i, j-1, nextTurn, s_s1, s_s2)
            if turn == 0:
                if first[0] -first[1] > second[0] - second[1]:
                    return first
                else:
                    return second
            else:
                if first[0] - first[1] > second[0]-second[1]:
                    return second
                else:
                    return first
        a,b =  pick(0, len(stones)-1, 0, 0, 0)
        return a-b
            
        
