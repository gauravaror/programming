class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:
        if len(self.bookings) == 0 or self.bookings[0][0] >= end:
            #print(start, end, self.bookings)
            self.bookings.insert(0, [start, end])
            return True
        idx = 1
        prev = self.bookings[0]
        replace_idx = True
        while idx < len(self.bookings):
            current = self.bookings[idx]
            #print("!", start,end, prev, current, self.bookings)
            if start < prev[0] and end > prev[0]:
                return False
            if start >= prev[0] and start < prev[1]:
                return False
            if start > prev[0] and end < prev[1]:
                return False
            if start > prev[0] and start < prev[1]:
                return False
            if start >= prev[1] and end <= current[0]:
                self.bookings.insert(idx, [start, end])
                return True
            if start < current[1]:
                return False            
            prev = current
            idx += 1
        if self.bookings[-1][1] <= start:
            self.bookings.append([start, end])
            return True
        return False
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
