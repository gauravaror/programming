class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_boxes = float('inf')
        min_region = [m, n]
        for i in ops:
            boxes = i[0]*i[1]
            min_region = [min(min_region[0], i[0]), min(min_region[1], i[1])]
        return min_region[0]*min_region[1]
