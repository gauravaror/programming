# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        start = 0
        end = m-1
        data = {}
        def checkanyone(col):
            if col in data:
                return data[col]
            allzero = True
            for i  in range(n):
                if binaryMatrix.get(i, col) == 1:
                    allzero = False
                    break
            data[col] = allzero
            return allzero
        print("mmmm", binaryMatrix)      
        data = {}
        while start < end:
            mid = (start + end)//2
            val = checkanyone(mid)     
            print(mid, start, end, val)
            if val:
                start = mid + 1
            else:
                end = mid
        print(data, start, end)
        if start  not in data:
            checkanyone(start)
        if data[start] == False:
            return start
        else:
            return -1
