class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        elem = min(A)
        S = 0
        while elem > 0:
            S += elem%10
            elem = elem//10
        if S %2 == 0:
            return 1
        else:
            return 0

