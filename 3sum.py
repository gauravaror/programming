from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], exclude: int, equal:int):
        hh = defaultdict(lambda: 0)
        out = []
        for idx,i in enumerate(nums):
            if idx == exclude:
                continue
            hh[i] += 1
        for idx,i in enumerate(nums):
            if idx == exclude:
                continue
            this_count = hh[i]
            #print("dsf", this_count, i, idx)
            if this_count > 1 and 2*i == equal:
                #print("dsdf", this_count, i, equal)
                out.append([i, i]) 
            if equal-i == i and this_count <=1:
                continue
            if equal-i in hh:
                out.append([i, equal-i])
        return out
        
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        overall = defaultdict(list)
        for idx,i in enumerate(nums):
            out = self.twoSum(nums, idx, -i)
            #print(i, idx, out)
            for output in out:
                output.append(i)
                output.sort()
                ha = sum([ (37**idx)*i for idx,i in enumerate(output)])
                overall[ha].append(output)
        #print(overall)
        return [i[0] for i in overall.values()]
