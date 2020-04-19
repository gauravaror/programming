class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        def findpartion():
            if len(nums) < 10 and len(nums) > 1:
                prev = 0
                for i in range(1, min(10, len(nums))):
                    if nums[prev] > nums[i]:
                        return prev
                    else:
                        prev = i
            start = 0
            end = len(nums)-1
            while start < end-3:
                mid = (start + end) // 2
                if nums[mid] < nums[0]:
                    end  = mid
                else:
                    start = mid
            prev = start
            breki =  -1
            print(start, end)
            for i in range(start+1, end+1):
                if nums[prev] > nums[i]:
                    breki = prev
                    break
                else:
                    prev = i
            return breki
        partition = findpartion()
        print("part ", partition)
        if partition == -1 or target < nums[0]:
            start = partition + 1
            end = len(nums) - 1
        else:
            start = 0
            end = partition
        print("searchin ", start, end)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return -1
