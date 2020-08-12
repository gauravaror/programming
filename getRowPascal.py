class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        k = 1
        if rowIndex == 0:
            return [1]
        prev = [0]*(rowIndex+1)
        prev[0] = 1
        new = [0]*(rowIndex+1)
        while k <= rowIndex:
            for i in range(k+1):
                if i == 0:
                    new[0] = 1
                elif i == k:
                    new[i] = 1
                else:
                    new[i] = prev[i] + prev[i-1]
            k += 1
            prev = new.copy()
        return new
