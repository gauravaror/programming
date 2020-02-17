class ProductOfNumbers:

    def __init__(self):
        self.prefix_array = []
        

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_array.clear()
        else:                
            prev = 1 if len(self.prefix_array) == 0 else self.prefix_array[0]
            self.prefix_array.insert(0, prev*num)
        
    def getProduct(self, k: int) -> int:
        pref_len = len(self.prefix_array)
        if pref_len < k:
            return 0
        elif pref_len == k:
            return int(self.prefix_array[0])
        else:
            return int(self.prefix_array[0]/self.prefix_array[k])
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
