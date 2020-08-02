import string
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        all_lower = all([ w in string.ascii_lowercase for w in word[1:]])
        all_upper = all([ w in string.ascii_uppercase for w in word[1:]])
        if word[0] in string.ascii_uppercase and all_upper:
            return True
        elif all_lower:
            return True
        else: 
            return False
