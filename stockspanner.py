class StockSpanner:

    def __init__(self):
        self.prices = []
        self.seq = []
        

    def next(self, price: int) -> int:
        if len(self.prices) == 0:
            self.prices.append(price)
            self.seq.append(1)
            return 1
        process = False if self.prices[-1] > price else True
        self.prices.append(price)
        if not process:
            self.seq.append(1)
            return 1
        else:
            start = len(self.prices)-2
            ans = 1
            #print(self.prices, start, price, self.prices[start])
            while (self.prices[start] <= price and start >= 0):
                #print(start)
                ans += self.seq[start]
                start -= self.seq[start]
            self.seq.append(ans)
            #print(ans)
            return ans
                
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
