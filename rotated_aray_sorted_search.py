class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        d = len(nums)//2
        if d == 0:
            d = 1
        start = 0
        end = len(nums)-1
        starting_elem = nums[0]
        while d >= 1:
            for j in range(start, end+1, d):
                if (nums[j] == target):
                    return True
                if (nums[j] > starting_elem):
                    start = j + 1
                elif (nums[j] < starting_elem):
                    end = j - 1
                else:
                    if nums[j] == nums[start]:
                        start = start + 1
                    elif nums[j] == nums[end]:
                        end = end - 1
                    
            d = d // 2
        print(start, end)
        if (target > nums[0]):
            start = 0
            end = end-1
        elif target < nums[0]:
            end = len(nums) - 1
        d = len(nums)//2
        if d == 0:
            d = 1
        print(start, end, d)
        while d >= 1:
            for j in range(start, end + 1, d):
                print(j, nums[j], target, d)
                if (nums[j] == target):
                    return True
                elif(nums[j] > target):
                    end = j - 1
                else:
                    start = j + 1
                if start == end and nums[start] == target:
                    return True
                    
            d = d//2
                
        return False
