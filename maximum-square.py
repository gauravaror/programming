class Solution:
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        new_level = [["0"]*cols for _ in range(rows)]
        any_four = False
        for i in range(rows-1):
            for j in range(cols-1):
                if matrix[i][j] =="1" and matrix[i+1][j] == "1" and matrix[i][j+1] == "1" and matrix[i+1][j+1] == "1":
                    any_four = True
                    new_level[i][j] = "1"
        if any_four:
            print("Calling maximal square", new_level)
            return self.maximalSquare1(new_level) + 1
        else:
            return 0
        
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_area = self.maximalSquare1(matrix)
        if len(matrix) == 0:
            return 0
        if max_area > 0:
            max_area = max_area + 1
        else:
            any_taker = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == "1":
                        any_taker = True
            if any_taker:
                max_area = 1
        return max_area**2
