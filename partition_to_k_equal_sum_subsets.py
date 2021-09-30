class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        each = total//k
        nums.sort(reverse=True)
        def backtrack(idx,sums):
            if any([i > each for i in sums]):
                return False
            if idx == len(nums):
                if all([i == each for i in sums]):
                    return True
            elif idx > len(nums):
                return False
            this_num = nums[idx]
            for i in range(len(sums)):
                backup = sums[i]
                sums[i] = sums[i] + this_num
                status = backtrack(idx+1, sums)
                sums[i] = backup
                if status:
                    return True
        return backtrack(0, [0]*k)
