class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        has = {}
        output = -1
        for idx,i in enumerate(s):
            if i in has:
                output = max(output,idx-has[i]-1)
            else:
                has[i] = idx
        return output
