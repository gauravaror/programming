from collections import defaultdict
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        tracker = defaultdict(int)
        min_size = float('inf')
        for idx,i in enumerate(nums):
            tracker[idx + len(nums)*idx] = nums[idx]
            if (nums[idx] >= s):
                return 1
            for jd,j in enumerate(nums[idx+1:]):
                jdx = idx + 1 + jd
                #print(idx, jdx, nums[idx], nums[jdx], tracker[idx][jdx-1] + nums[jdx])
                tracker[idx + len(nums)*jdx] = tracker[idx + len(nums)*(jdx-1)] + nums[jdx]
                if tracker[idx + len(nums)*jdx] >= s:
                    if jdx-idx+1 < min_size:
                        min_size = jdx-idx + 1
            tracker.clear()
        if min_size == float('inf'):
            return 0
        return min_size

