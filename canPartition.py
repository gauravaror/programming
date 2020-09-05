class Solution:
    def solve(self, set1, set2, index):
        if (set1,set2,index) in self.dp:
            return
        if index >= len(self.nums):
            return
        if set1 + self.reversePrefixSum[index] < set2:
            return
        if set2 + self.reversePrefixSum[index] < set1:
            return
        if index == len(self.nums)-1:
            if set1 + self.nums[index] == set2:
                self.can = True
            if set2 + self.nums[index] == set1:
                self.can = True
        self.solve(set1 + self.nums[index], set2, index+1)
        self.solve(set1, set2 + self.nums[index], index+1)
        self.dp[set1,set2,index] = True
    
    def canPartition(self, nums: List[int]) -> bool:
        
        cumsum = 0
        ra  = []
        for i in range(len(nums)-1,-1,-1):
            cumsum += nums[i]
            ra.append(cumsum)
        self.reversePrefixSum = ra[::-1]
        self.dp = {}
        self.nums = nums
        self.can = False
        self.solve(0, 0, 0)
        return self.can
