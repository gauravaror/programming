class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print([ list(a)[::-1] for a in zip(*matrix)])
        matrix[:] = zip(*matrix[::-1])
        #matrix = matrix1
