class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        sample_rows = {}
        sample_cols = {}
        for i in range(rows):
            min_index = 0
            for j in range(1,cols):
                if matrix[i][min_index] > matrix[i][j]:
                    min_index=j
            sample_rows[(i,min_index)] = True
        for i in range(cols):
            min_index = 0
            for j in range(1,rows):
                if matrix[min_index][i] < matrix[j][i]:
                    min_index=j
            sample_cols[(min_index,i)] = True
        answer = []
        #print(sample_rows, sample_cols)
        for i in sample_rows:
            if i in sample_cols:
                answer.append(matrix[i[0]][i[1]])
        return answer
