class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory = sorted(inventory)
        num_balls = 1
        earn = 0
        index = len(inventory) - 1
        def get_balls(a):
            return a*(a+1)//2
        print(inventory)
        while index >= 0 and orders > 0:
            if index == 0:
                diff_balls = inventory[index]
            else:
                diff_balls = inventory[index] - inventory[index-1]
            
            if index != 0 and orders >= num_balls*diff_balls:
                orders -= num_balls*(inventory[index] - inventory[index-1])
                earn += num_balls*(get_balls(inventory[index]) - get_balls(inventory[index-1]))
                num_balls += 1
            else:
                div_orders = orders - orders%num_balls
                rem_order = orders%num_balls
                if rem_order > 0:
                    earn += num_balls*(get_balls(inventory[index]) - get_balls(inventory[index] - div_orders//num_balls))
                    earn += rem_order*(inventory[index] - div_orders//num_balls)
                else:
                    print(inventory[index] - div_orders//num_balls, get_balls(inventory[index]) , get_balls(inventory[index] - div_orders//num_balls))
                    earn += num_balls*(get_balls(inventory[index]) - get_balls(inventory[index] - div_orders//num_balls))
                
                orders = 0
            index -= 1
            #print(index, orders, diff_balls, num_balls, earn)
        return earn% (pow(10,9) + 7)
                
                
                
            
        
