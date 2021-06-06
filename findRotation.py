class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotateBy90(matrix):
            all_same = True
            new_mat = deepcopy(matrix)
            for i in range(len(new_mat)):
                row = matrix[i]
                for j in range(len(matrix[0])):
                    new_mat[j][len(new_mat) - i- 1] = row[j]
                    if target[j][len(new_mat) -i- 1] != row[j]:
                        all_same = False
            return new_mat, all_same
        fir, g = rotateBy90(mat)
        if g:
            return True
        sec,g = rotateBy90(fir)
        if g:
            return True
        thr,g = rotateBy90(sec)
        if g:
            return True
        four,g = rotateBy90(thr)
        if g:
            return True
        return False
                
