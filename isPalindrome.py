import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = filter(lambda a: a.isalnum(), s)
        snew1 = map(lambda a: a if not (a in string.ascii_uppercase) else string.ascii_lowercase[string.ascii_uppercase.index(a)], list(snew))
        news = list(snew1)
        if news == news[::-1]:
            return True
        else:
            return False
