class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            current_num = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > -current_num:
                    end -= 1
                elif nums[start] + nums[end] < -current_num:
                    start += 1
                else:
                    sol = [current_num, nums[start], nums[end]]
                    solutions.append(sol)
                    start += 1
                    end -= 1
                    while start < len(nums) -1 and nums[start] == nums[start-1]:
                        start += 1
                    while end > 0 and nums[end] == nums[end+1]:
                        end -= 1
        return solutions
