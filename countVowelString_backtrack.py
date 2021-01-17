class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = 0
        def back(index, length):
            nonlocal ans
            if index >= 5:
                return
            if length == n:
                ans += 1
                return
            for i in range(5):
                back(index+i, length+1)
        back(0,0)
        return ans
