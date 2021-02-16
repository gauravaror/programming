class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        nrows = len(mat)
        data = []
        for i in range(nrows):
            data.append((sum(mat[i]), i))
        data.sort()
        return [data[i][1] for i in range(k)]
            
        
