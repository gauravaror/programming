class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        yra1, ma1, da1 =  date1.split('-')
        yra2, ma2, da2 =  date2.split('-')
        yr1, m1, d1 = int(yra1), int(ma1), int(da1)
        yr2, m2, d2 = int(yra2), int(ma2), int(da2)
        correctOrder = False
        if yr1 < yr2:
            correctOrder = True
        elif yr1 == yr2:
            if m1 < m2:
                correctOrder = True
            elif m1 == m2:
                if d1 < d2:
                    correctOrder = True
                elif d1 == d2:
                    return 0
        if not correctOrder:
            yr1, m1, d1 = int(yra2), int(ma2), int(da2)
            yr2, m2, d2 = int(yra1), int(ma1), int(da1)
        days = 0
        day_months = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,9:30, 10:31, 11:30, 12:31}
        def isLeapYear(year):
            if ((i % 4 == 0) and (i%100 != 0)) or (i%400 ==0):
                return True
            else:
                return False
        if not yr1 == yr2:
            whole_years = (yr2-yr1-1)
            days = whole_years*365
            #leap_years = whole_years//4
            #days += leap_years
            for i in range(yr1+1, yr2):
                if isLeapYear(i):
                    days += 1
                    
        print("after years", days)
        if not m1 == m2 or not yr1 == yr2:
            for i in range(m1+1, 12+1):
                days += day_months[i]
                if i == 2 and isLeapYear(yr1):
                    days += 1
            for i in range(1, m2):
                days += day_months[i]
                if i == 2 and isLeapYear(yr2):
                    days += 1
        print("after months", days)
        if not m1 == m2 or not yr1 == yr2 or not d1 == d2:
            if not (m1 == m2 and yr1 == yr2):
                days += day_months[m1] - d1
                days += d2
            else:
                days += d2 - d1
        print("after days", days)
        return days
