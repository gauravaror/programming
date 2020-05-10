from collections import Counter
from decimal import *
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        def get_slope(c1, c2):
            sl = c2[1]  - c1[1]
            ina = c2[0] - c1[0]
            slope = 0 if ina == 0 else Decimal(sl)/Decimal(ina)
            intercept = c2[0] if ina == 0 else c2[1] - slope*c2[0]
            #print(slope, intercept, ina, c2,c2[1] - slope*c2[0])
            line_id = slope + 37*intercept
            slope = slope
            line_id = line_id
            intercept = intercept
            return line_id, sl, ina, c1
        c = Counter()
        hh = {}
        for i in range(1, len(points)):
            for j in range(i):
                lid, sl, ina, ince = get_slope(points[i], points[j])
                #print(lid, sl, ince)
                c[lid] += 1
                if lid not in hh:
                    hh[lid] = (sl, ina, ince)
        print(c)
        m, m2, b = hh[c.most_common()[0][0]]
        pp = 0
        print(c.most_common())
        output = {}
        for i in points:
            diff = m2*(i[1] - b[1]) - m*(i[0] - b[0])
            diff1 = round(i[1] - b[1] - m*(i[0] - b[0]),4)
            print(i, m, b,diff, diff1, diff == 0, pp)
            if m == 0:
                if b[0] == i[0] or diff == 0:
                    pp += 1
            elif diff == 0:
                pp += 1
        return pp
