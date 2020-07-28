class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        non_grumpy = 0
        for c,g in zip(customers, grumpy):
            if g == 0:
                non_grumpy += c
        #print("Non grumpy things", non_grumpy)
        start = 0
        end = X-1
        cgrumpy = 0
        for i in range(start, end+1):
            if grumpy[i] == 1:
                cgrumpy += customers[i]
            
        output = non_grumpy + cgrumpy
        while end <= len(grumpy)- 2:
            #print(start, output)
            if grumpy[start] == 1:
                cgrumpy -= customers[start]
            if grumpy[end +1] == 1:
                cgrumpy += customers[end+1]
            start += 1
            end += 1
            output = max(output, non_grumpy + cgrumpy)
            
        return output
