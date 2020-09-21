class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        pending_ends = []
        current_peeps = 0
        start = None
        for i in trips:
            while pending_ends and pending_ends[0][0] <= i[1]:
                item = heapq.heappop(pending_ends)
                current_peeps -= item[1]
            if current_peeps + i[0] > capacity:
                return False
            start = i[1]
            heapq.heappush(pending_ends, (i[2], i[0]))
            current_peeps += i[0]
        return True 
