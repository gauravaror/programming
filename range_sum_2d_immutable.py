### Accepted solution
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sum_from_origin = {}
        self.num_rows = len(matrix)
        if self.num_rows == 0:
            return
        self.num_cols = len(matrix[0])
        print(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                current_sum = 0
                if i > 0:
                    current_sum += self.sum_from_origin[(i-1,j)]
                if j > 0:
                    current_sum += self.sum_from_origin[(i,j-1)]
                if i > 0  and j > 0:    
                    current_sum -= self.sum_from_origin[(i-1, j-1)]
                current_sum += matrix[i][j]
                self.sum_from_origin[(i,j)] = current_sum
                #print("Sum at ",i, j, current_sum)
                    
                
    
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        print(row1, col1, row2, col2)
        if row1 == 0 and col1 == 0 :
            return self.sum_from_origin[(row2, col2)]
        elif row1 == 0:
            return self.sum_from_origin[(row2,col2)] - self.sum_from_origin[(row2, col1-1)]
        elif col1 == 0:
            return self.sum_from_origin[(row2,col2)] - self.sum_from_origin[(row1-1,col2)]
            
        main_area = self.sum_from_origin[(row2,col2)]
        sub1_area = self.sum_from_origin[(row2,col1-1)]
        sub2_area = self.sum_from_origin[(row1-1,col2)]
        add_area = self.sum_from_origin[(row1-1,col1-1)]
        ans = main_area - sub1_area - sub2_area + add_area
        print(main_area, sub1_area, sub2_area, add_area, ans)
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
