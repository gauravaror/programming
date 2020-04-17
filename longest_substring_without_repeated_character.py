from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        count = Counter()
        max_length = 0
        while start < len(s):
            if end < len(s) and count[s[end]] == 0 and ((len(count) == 0) or (len(count) > 0 and count.most_common()[0][1] <= 1)):
                count.update(s[end])
                end += 1
                if (end -start) > max_length:
                    max_length = end - start
            else:
                count.subtract(s[start])
                start += 1
            #print(start, end, count)
        return max_length
