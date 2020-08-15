class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # string, position we are at and number of edits left
        # pos = current position
        # ka = edit available
        # la = current length
        self.maxlen = 0
        def back(s, lastchar,pos, ka, la):
            if la > self.maxlen:
                self.maxlen = la
            if pos >= len(s):
                return
            if lastchar == s[pos]:
                back(s, s[pos], pos+1, ka, la+1)
            else:
                if ka != 0: back(s, lastchar, pos+1, ka-1, la+1)
                back(s, s[pos], pos+1, k, 1)
        back(s, s[0], 1, k, 1)
        return self.maxlen
