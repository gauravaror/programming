class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        matchsticks.sort(reverse=True)
        each = total//4
        print(total, total%4)
        if total % 4  != 0:
            return False
        @lru_cache(None)
        def backtrack(index, s):
            if index == len(matchsticks):
                if s[0] == s[1] and s[0] == s[1] and s[0] == s[2] and s[0] == s[3]:
                    return True
                return False
            if s[0] > each or s[1] > each or s[2] >  each or s[3] > each:
                return False
            d = matchsticks[index]
            if s[0] + d <= each:
                a = backtrack(index+1, (s[0] + d, s[1], s[2], s[3]))
                if a:
                    return a
            if s[1] + d <= each:
                b = backtrack(index+1, (s[0], s[1] + d, s[2], s[3]))
                if b:
                    return b
            if s[2] + d <= each:
                c = backtrack(index+1, (s[0], s[1], s[2] + d, s[3]))
                if c:
                    return c
            if s[3] + d <= each:
                d = backtrack(index+1, (s[0], s[1], s[2], s[3] + d))
                if d:
                    return d
        return backtrack(0, (0,0,0,0))
        
