class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lnum = len(s)//2
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        countn = lambda st: sum([1 if f in vowels else 0 for f in st])
        return True if countn(s[:lnum]) == countn(s[lnum:]) else False 
