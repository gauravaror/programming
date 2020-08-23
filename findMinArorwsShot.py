class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points = sorted(points)
        start, end = points[0]
        arrows = 1
        for i in points[1:]:
            if i[0] <= end:
                start = max(start, i[0])
                end = min(end, i[1])
            else:
                arrows += 1
                start, end = i
        return arrows
