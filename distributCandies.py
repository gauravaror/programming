class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        round_val = n*(n+1)//2
        round_ = n*(n+1)//2
        output = [0]*n
        full_round = 0
        while round_ < candies:
            full_round += 1
            round_ += n*n*full_round + round_val
            #print("FR", full_round, round_)
            
        if full_round > 0:
            for i in range(n):
                output[i] = ((full_round*(full_round -1))//2)*n + (i+1)*full_round
        #print(round_, sum(output))
        remaining = candies-sum(output)
        #print(full_round, output, remaining)
        for i in range(n):
            #print(i, full_round, n)
            if n*full_round + (i+1) < remaining:
                output[i] += n*full_round + (i+1)
                remaining -= n*full_round + (i+1)
            else:
                #print("b", output, remaining)
                output[i] += remaining
                #print(output)
                return output
        return output
