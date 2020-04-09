from collections import defaultdict
class Solution:        
    def init(self, nums):
        self.nums = nums
        self.hh = defaultdict(lambda: 0)
        self.indexes = defaultdict(list)
        for idx,i in enumerate(nums):
            self.hh[i] += 1
            self.indexes[i].append(idx)
        
    def twoSum(self, nums: List[int], exclude: int, equal:int):
        out = []
        for idx,i in enumerate(nums):
            if idx == exclude:
                continue
            this_count = self.hh[i]
            if equal-i == i and i == nums[exclude] and this_count <= 2:
                continue
            if this_count > 1 and 2*i == equal:
                out.append([i, i]) 
            if equal-i == i and this_count <=1:
                continue
            if equal-i in self.hh and (len(self.indexes[equal-i]) >  1 or exclude not in self.indexes[equal-i]):
                out.append([i, equal-i])
        return out
        
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.init(nums)
        overall = defaultdict(list)
        seen = {}
        for idx,i in enumerate(nums):
            if i in seen:
                continue
            else:
                seen[i] = 1
            out = self.twoSum(nums, idx, -i)
            for output in out:
                output.append(i)
                output.sort()
                ha = sum([ (37**idx)*i for idx,i in enumerate(output)])
                overall[ha].append(output)
        return [i[0] for i in overall.values()]
############################## ATTEMPT 1 ########################################3

from collections import defaultdict
class Solution1:
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
