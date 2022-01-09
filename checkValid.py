class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        nrows = len(matrix)
        expected = (nrows*(nrows+1))/2
        trans = list(zip(*matrix))
        for i in range(nrows):
            #print(sum(matrix[i]), sum(trans[i]), matrix[i], trans[i])
            if sum(matrix[i]) != expected or set(matrix[i]) != set(range(1,nrows+1)):
                return False
            if sum(trans[i]) != expected or set(trans[i]) != set(range(1,nrows+1)):
                return False
        return True
