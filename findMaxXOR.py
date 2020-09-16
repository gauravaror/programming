class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0
        tries = {}
        for i in nums:
            node = tries
            for j in range(31,-1,-1):
                activ_bit = int(i&(1<<j) > 0)
                if activ_bit in node:
                    node = node[activ_bit]
                else:
                    node[activ_bit] = {}
                    node = node[activ_bit]
        global_max = 0
        #print(tries)
        for i in nums:
            node = tries
            th_sum = 0
            for j in range(31,-1,-1):
                activ_bit = int(i&(1<<j) > 0)
                neg_activ_bit = activ_bit^1
                if neg_activ_bit in node:
                    th_sum += (1<<j)
                    node = node[neg_activ_bit]
                else:
                    node = node[activ_bit]
                #print(i, th_sum,j, node, activ_bit, neg_activ_bit)
            global_max = max(global_max, th_sum)
        return global_max
