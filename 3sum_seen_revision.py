class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solutions = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                #print(start, end, i)
                tot = nums[start] + nums[end] + nums[i]
                if tot > 0:
                    end -= 1
                elif tot < 0:
                    start += 1
                else:
                    solutions.append([nums[start], nums[end], nums[i]])
                    start += 1
                    end -= 1
                    while start < len(nums)-1 and nums[start] == nums[start-1]:
                        start += 1
                    while end > 0 and nums[end] == nums[end+1]:
                        end -= 1
        return solutions
