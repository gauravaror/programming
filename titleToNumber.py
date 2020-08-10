import string
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for idx,i in enumerate(s[::-1]):
            letter_index = string.ascii_uppercase.index(i) + 1
            ans += pow(26, idx)*letter_index
        return ans
