from collections import Counter
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = Counter()
        cols = Counter()
        for point in indices:
            rows[point[0]] += 1
            cols[point[1]] += 1
        print(rows, cols)
        num_odd = 0
        for ri in range(n):
            for ci in range(m):
                if not (rows[ri] + cols[ci]) % 2 == 0:
                    num_odd += 1
        return num_odd
