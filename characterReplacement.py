from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(lambda: 0)
        start = 0
        end = 0
        most_frequent = 0
        maxlen = 0
        while end <= len(s):
            change_needed  = end - start - most_frequent
            if change_needed <= k:
                maxlen = max(maxlen, end-start)
            if end == len(s):
                break
            if change_needed > k:
                chars[s[start]] -= 1
                start += 1
            else:
                chars[s[end]] += 1
                end += 1
            most_frequent = max(chars.values())
        return maxlen
