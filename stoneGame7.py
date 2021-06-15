class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix_sum = list(accumulate(stones))
        @lru_cache(10000)
        def pick(i, j):
            if i == j:
                return 0
            turn = (len(stones) - (j-i+1) ) % 2
            add_1 = prefix_sum[j] - prefix_sum[i]
            first = pick(i+1, j)
            
            a = prefix_sum[i-1] if i > 0 else 0
            add_2 = prefix_sum[j-1] - a
            second = pick(i, j-1)
            if turn == 0:
                return max(first + add_1, second + add_2)
            else:
                return min(first - add_1, second - add_2)
        ans =  pick(0, len(stones)-1)
        return ans
