# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        all_zeros = True
        n,m = binaryMatrix.dimensions()
        last_non_zero = -1
        
        for i in range(n):
            if binaryMatrix.get(i, m-1) != 0:
                all_zeros = False
                last_non_zero = i
        if all_zeros:
            return -1
        first_nonzero_index = -1
        for i in range(m):
            if binaryMatrix.get(last_non_zero, i):
                first_nonzero_index = i
                break
        if first_nonzero_index == 0:
            return 0
        print(last_non_zero, first_nonzero_index)
        for i in range(first_nonzero_index+1):
            for j in range(n):
                if binaryMatrix.get(j, i) == 1:
                    return i
        return -1
