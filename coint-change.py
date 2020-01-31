class Solution:
    def __init__(self):
        self.sol_map = {}
        self.coins = None
         
    def get_coin(self, amount):
        if amount in self.sol_map:
            return self.sol_map[amount]
        min_coin = float('inf')
        for i in self.coins:
            if (amount-i) == 0:
                ans = 0
            elif (amount-i) < 0:
                ans = float('inf')
            else:
                ans = self.get_coin(amount-i)
            if (ans + 1) < min_coin:
                min_coin  = ans + 1
        self.sol_map[amount] = min_coin
        return min_coin
                    
                
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        if amount == 0:
            return 0
        coint =  self.get_coin(amount)
        if coint == float('inf'):
            return -1
        return coint
