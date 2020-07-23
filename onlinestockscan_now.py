class StockSpanner:

    def __init__(self):
        self.nums = []
        self.smaller = []
        

    def next(self, price: int) -> int:
        if len(self.nums) == 0:
            self.nums.append(price)
            self.smaller.append(-100)
            return 1
        else:
            sta = 0
            le = len(self.nums) - 1
            while le-sta >= 0 and self.nums[le-sta] <= price:
                if self.smaller[le-sta] == -100:
                    sta += 1
                    break
                sta += self.smaller[le-sta]
            sta += 1
            self.nums.append(price)
            self.smaller.append(sta)
            return sta
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
