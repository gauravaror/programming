from heapq import heappush, heappop
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        if len(days) == 0:
            return 0
        day = 0
        att = []
        eaten = 0
        print(apples, days)
        while day < len(days) or len(att) > 0:
            if day  < len(days):
                ap = apples[day]
                exp = day + days[day]
                if ap > 0:
                    heappush(att, (exp, ap))
            while att and att[0][0] <= day:
                heappop(att)
            if len(att) > 0:
                rexp = heappop(att)
                eaten += 1
                if rexp[1] - 1 > 0:
                    heappush(att, (rexp[0], rexp[1] - 1))
            day += 1
        return eaten
        
