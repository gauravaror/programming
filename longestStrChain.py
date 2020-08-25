
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        print(words)
        dp = [1]*len(words)
        def is_chain(word1, word2):
            if len(word1) != len(word2) + 1:
                return False
            p1 = 0
            p2 = 0
            diff = 0
            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] == word2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1
                    diff += 1
            if p1 == len(word1) and p2 == len(word2) and diff == 1:
                return True
            elif p1 == len(word1)-1 and p2 == len(word2) and diff == 0:
                return True
            return False
            
        for i in range(1, len(words)):
            for j in range(i):
                if is_chain(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)
