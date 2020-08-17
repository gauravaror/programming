class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        start = 0
        end = min(len(str1), len(str2))
        while start < end and str1[start] == str2[start]:
            start += 1
        def isGCD(st):
            lst1 = len(str1)//len(st)
            lst2 = len(str2)//len(st)
            if not st*lst1 == str1:
                return False
            if not st*lst2 == str2:
                return False
            return True
        while start >0:
            if isGCD(str1[:start]):
                return str1[:start]
            start -= 1
        return ""
