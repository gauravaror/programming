from collections import Counter
from decimal import *
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def generateGCD(x, y):
            if y == 0:
                return x
            else:
                return generateGCD(y, x%y)
        if len(points) <= 2:
            return len(points)
        def get_slope(c1, c2):
            sl = c2[1]  - c1[1]
            ina = c2[0] - c1[0]
            gcd = generateGCD(sl, ina)
            if (gcd != 0):
                sl = sl/gcd
                ina = ina/gcd
            line_id = sl + 37*ina
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
        m, m2, b = hh[c.most_common()[0][0]]
        pp = 0
        output = {}
        for i in points:
            diff = m2*(i[1] - b[1]) - m*(i[0] - b[0])
            diff1 = round(i[1] - b[1] - m*(i[0] - b[0]),4)
            if m == 0:
                if b[0] == i[0] or diff == 0:
                    pp += 1
            elif diff == 0:
                pp += 1
        return pp
