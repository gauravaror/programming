from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxlen = 0
        c = Counter()
        while start < len(s):
            print(start, end)
            if end <= len(s)-1 and c[s[end]] == 0:
                c[s[end]] += 1
                maxlen = max(maxlen, end-start+1)
                end += 1
            else:
                c[s[start]] -= 1
                start += 1
        print(start, end)
        return maxlen
