class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        chars = Counter()
        maxlen = 0
        while end < len(s):
            if chars[s[end]] < 1:
                chars[s[end]] += 1
                end += 1
            else:
                while s[start] != s[end]:
                    chars[s[start]] -= 1
                    start += 1
                chars[s[start]] -= 1
                start += 1
            #print(start, end, chars)
            maxlen = max(maxlen, end-start)
        return maxlen
