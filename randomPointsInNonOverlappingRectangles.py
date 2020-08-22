import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rectangles = rects
        self.areas = []
        totalarea = 0
        for idx,i in enumerate(rects):
            x1,y1,x2,y2 = i
            area = abs(y2-y1 + 1)*abs(x2-x1+1)
            totalarea += area
            self.areas.append(totalarea)
        

    def pick(self) -> List[int]:
        genrect = random.randint(0, self.areas[-1])
        start = 0
        end = len(self.areas)-1
        while start < end:
            mid = start + (end-start)//2
            if self.areas[mid] >= genrect:
                end = mid
            else:
                start = mid + 1
        nowrec = self.rectangles[start]
        ina = random.randint(nowrec[0], nowrec[2])
        ina2 = random.randint(nowrec[1], nowrec[3])
        return ina, ina2
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
