class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        if n % 2 != 0:
            output.append(0)
        for i in range(1, n//2 +1):
            output.append(i)
            output.append(-i)
        return output
