class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) <= 1:
            return False
        pointer = k+1
        initial = nums[:k+1]
        #print(initial)
        initial.sort()
        if len(nums) < k+1:
            k = len(nums)-1

        def bs(arr, num):
            start = 0
            end = len(arr)
            while start < end:
                mid = start + (end-start)//2
                if arr[mid] >= num:
                    end = mid
                else:
                    start = mid + 1
            return start

        for i in range(k):
            for j in range(i+1,k+1):
                #print(initial[i], initial[j], abs(initial[i] - initial[j]) <= t)
                if abs(initial[i] - initial[j]) <= t:
                    return True

        while pointer < len(nums):
            pos = bs(initial, nums[pointer-(k+1)])
            #print("del", initial, pointer-(k+1), nums[pointer-(k+1)], pos)
            del initial[pos]
            pos = bs(initial, nums[pointer])
            #print(pointer, initial, pos)
            if pos < len(initial) and abs(initial[pos] - nums[pointer])  <= t:
                return True
            if pos-1 >= 0:
                if abs(initial[pos-1] - nums[pointer])  <= t:
                    return True
            if pos + 1 < len(initial):
                if abs(initial[pos+1] - nums[pointer]) <= t:
                    return True
            initial.insert(pos, nums[pointer])
            pointer += 1
            
        return False
