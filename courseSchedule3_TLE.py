class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        print(courses)
        courses = sorted(courses, key=lambda x: x[1])
        last_closing = max(courses, key=lambda x: x[1])[1]
        dp = [0]*(last_closing + 1)
        dpold = [0]*last_closing
        for course in courses:
            for time in range(last_closing+1):
                if time <= course[1] and time-course[0] >= 0:
                    dp[time] = max(dp[time], dpold[time - course[0]] + 1)
                elif time-1 >= 0:
                    dp[time] = max(dp[time], dp[time-1])
            dpold = dp.copy()
            #print(dp)
        return dp[-1]
