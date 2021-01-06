class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currtime = 1
        wait = 0
        for arrival, prep in customers:
            if currtime < arrival:
                currtime = arrival
            currtime += prep
            wait += (currtime-arrival)
        return wait/len(customers)
            
            
        
