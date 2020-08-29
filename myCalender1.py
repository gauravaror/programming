class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []
        
    def bs(self, array, target):
        start = 0
        end = len(array)
        while start < end:
            mid = start + (end-start)//2
            if array[mid] > target:
                end = mid
            else:
                start = mid + 1
        return start
        
    def book(self, start: int, end: int) -> bool:
        if len(self.starts) == 0:
            self.starts.append(start)
            self.ends.append(end)
            return True
        starting_index = self.bs(self.starts, start)
        ending_index = self.bs(self.ends, end)
        new_meeting_index = self.bs(self.ends, start)
        #print(self.starts, self.ends, starting_index, ending_index, new_meeting_index)
        if new_meeting_index != starting_index:
            return False
        if starting_index != ending_index:
            return False
        if starting_index < len(self.starts) and self.starts[starting_index] > start and self.starts[ending_index] < end:
            return False
        self.starts.insert(starting_index, start)
        self.ends.insert(ending_index, end)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
