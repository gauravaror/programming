class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        hh = {}
        output = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and k!=0:
                continue
            #print(nums[i], k, hh, output)
            if (nums[i] - k) in hh:
                output.add((nums[i],nums[i]-k))
            hh[nums[i]] = True
        #print(nums, len(output), output)
        return len(output)
