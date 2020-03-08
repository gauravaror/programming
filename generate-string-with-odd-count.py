class Solution:
    def get_lengths(self, n):
        if n % 2 == 0:
            return [n-1, 1]
        first= n//2
        second = n-first
        arr = []
        if not first % 2 == 0:
            arr.append(first)
        else:
            arr.extend(self.get_lengths(first))
        if not second % 2 == 0:
            arr.append(second)
        else:
            arr.extend(self.get_lengths(second))
        return arr
            
        
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'a'
        array = self.get_lengths(n)
        answer = []
        for idx,a in enumerate(array):
            char = chr(97+idx)
            answer.extend([char]*a)
        return ''.join(answer)
# https://leetcode.com/contest/weekly-contest-179/problems/generate-a-string-with-characters-that-have-odd-counts/
