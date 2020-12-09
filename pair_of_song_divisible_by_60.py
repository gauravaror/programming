class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hh = Counter()
        output = 0
        for i in time:
            this_rem = i%60
            if ((60-this_rem)%60) in hh:
                output += hh[((60-this_rem)%60)]
            hh[this_rem] += 1
        return output
            
        
