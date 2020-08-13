class Solution:
    def countVowelPermutation(self, n: int) -> int:
        def valid_chars(s):
            if len(s) == 0:
                return ['a', 'e', 'i', 'o', 'u']
            elif s[-1] == 'a':
                return ['e']
            elif s[-1] == 'e':
                return ['a', 'i']
            elif s[-1] == 'i':
                return ['a', 'e', 'o', 'u']
            elif s[-1] == 'o':
                return ['i', 'u']
            else:
                return ['a']
        self.outputs = 0
        def back(s):
            if len(s) == n:
                self.outputs += 1
                return
            for ne in valid_chars(s):
                back(s+ne)
        back('')
        return self.outputs % (1000000007)
